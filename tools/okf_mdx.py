"""MDX -> plain Markdown conversion.

The upstream docs are Docusaurus MDX: they import partials, wrap alternative
instructions in <Tabs>/<TabItem>, render Javadoc links through a React
component, and — in the getting-started pages — generate whole sections from
JavaScript helpers defined in `export const` preludes.  None of that survives a
plain Markdown reader, so each page is flattened into self-contained Markdown
before it becomes an OKF concept.

Where an expression cannot be resolved the original text is kept rather than
guessed at, so the output never invents content.
"""

from __future__ import annotations

import json
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.S)
IMPORT_RE = re.compile(r"^import\s+(?:(\w+)|\{[^}]*\})\s+from\s+['\"]([^'\"]+)['\"];?\s*$", re.M)
MDX_COMMENT_RE = re.compile(r"\{/\*.*?\*/\}", re.S)
ATTR_RE = re.compile(r"""(\w+)\s*=\s*(?:"([^"]*)"|'([^']*)'|\{`([^`]*)`\}|\{([^}]*)\})""")

THEME_PREFIXES = ("@theme/", "@site/", "@docusaurus/", "react")
PARTIAL_SUFFIXES = (".md", ".mdx")
NODE_TIMEOUT = 20


@dataclass
class Conversion:
    """Result of flattening one MDX page."""

    frontmatter: str
    body: str
    unresolved: set[str] = field(default_factory=set)


def split_frontmatter(text: str) -> tuple[str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return "", text
    return m.group(1), text[m.end():]


def _attrs(raw: str | None) -> dict[str, str]:
    if not raw:
        return {}
    out: dict[str, str] = {}
    for m in ATTR_RE.finditer(raw):
        value = next((g for g in m.groups()[1:] if g is not None), "")
        out[m.group(1)] = value.strip().strip("'\"")
    return out


def _replace_component(text: str, name: str, render) -> str:
    """Replace every <Name .../> and <Name ...>children</Name> via ``render``.

    ``render(attrs, children)`` returns the Markdown that takes its place.
    Paired tags are resolved innermost-first so nesting works.
    """
    paired = re.compile(rf"<{name}(\s[^>]*?)?>((?:(?!<{name}[\s/>]).)*?)</{name}>", re.S)
    selfclosing = re.compile(rf"<{name}(\s[^>]*?)?/>")

    for _ in range(12):
        new = paired.sub(lambda m: render(_attrs(m.group(1)), m.group(2)), text)
        if new == text:
            break
        text = new
    return selfclosing.sub(lambda m: render(_attrs(m.group(1)), ""), text)


# --------------------------------------------------------------------------
# JS prelude handling
# --------------------------------------------------------------------------

# Only a JavaScript declaration counts. Shell examples in the docs contain
# lines such as `export NAMESPACE=scalardb`, which must not be mistaken for one.
_EXPORT_DECL = re.compile(r"export\s+(?:const|let|var|function|default|async)\b")


def strip_export_prelude(body: str) -> tuple[list[str], str]:
    """Split ``export const ...`` declarations out of an MDX body.

    Returns (declarations, remaining_body).  Declarations may span many lines,
    so the scan tracks bracket depth and string/template state.  Callers must
    mask fenced code blocks first so that code samples are ignored.
    """
    prelude: list[str] = []
    out: list[str] = []
    i = 0
    n = len(body)
    while i < n:
        line_start = body.rfind("\n", 0, i) + 1
        if i != line_start or not _EXPORT_DECL.match(body, i):
            nl = body.find("\n", i)
            if nl == -1:
                out.append(body[i:])
                break
            out.append(body[i : nl + 1])
            i = nl + 1
            continue

        # A declaration runs until the terminating semicolon at depth 0.  As a
        # guard against a malformed prelude swallowing the page, the scan also
        # stops at a line that starts the JSX body.
        j = i
        depth = 0
        quote: str | None = None
        while j < n:
            ch = body[j]
            if quote:
                if ch == "\\":
                    j += 2
                    continue
                if ch == quote:
                    quote = None
            elif ch in "\"'`":
                quote = ch
            elif ch in "{[(":
                depth += 1
            elif ch in "}])":
                depth -= 1
            elif ch == ";" and depth <= 0:
                j += 1
                break
            elif ch == "\n" and depth <= 0:
                nxt = body[j + 1 :].lstrip(" \t")
                if nxt.startswith("<") or nxt.startswith("export "):
                    break
            j += 1
        prelude.append(body[i:j])
        i = j

    return prelude, "".join(out)


def js_safe_prelude(decls: list[str], jsx_defs: dict) -> str:
    """Drop declarations whose body is JSX before handing the prelude to node.

    A single JSX-returning helper would make the whole ``node -e`` script a
    syntax error and silently disable every interpolation on the page; those
    helpers are expanded textually by ``_expand_prelude_jsx`` instead.
    """
    kept = []
    for decl in decls:
        m = re.search(r"const\s+(\w+)", decl)
        if m and m.group(1) in jsx_defs:
            continue
        kept.append(decl)
    return "\n".join(kept)


_PRELUDE_ARROW = re.compile(r"const\s+(\w+)\s*=\s*(?:\(([^)]*)\)|(\w+))\s*=>\s*\(")


def parse_prelude_jsx(prelude: str) -> dict[str, tuple[list[str], str]]:
    """Find ``const Name = (args) => ( <jsx/> );`` definitions in a prelude.

    These are MDX-local React components (and helpers returning JSX) that carry
    real documentation text, so their bodies are inlined rather than dropped.
    """
    defs: dict[str, tuple[list[str], str]] = {}
    for m in _PRELUDE_ARROW.finditer(prelude):
        name = m.group(1)
        raw_params = m.group(2) if m.group(2) is not None else (m.group(3) or "")
        params = [
            p.strip()
            for p in raw_params.replace("{", "").replace("}", "").split(",")
            if p.strip()
        ]
        open_at = m.end() - 1
        depth = 0
        for i in range(open_at, len(prelude)):
            if prelude[i] == "(":
                depth += 1
            elif prelude[i] == ")":
                depth -= 1
                if depth == 0:
                    inner = prelude[open_at + 1 : i].strip()
                    if inner.startswith("<"):
                        defs[name] = (params, inner)
                    break
    return defs


def dedent_block(text: str) -> str:
    """Drop the common leading indentation of a block lifted out of JSX.

    MDX indents component children to match the surrounding markup.  Left in
    place, four or more spaces would turn ordinary prose into a Markdown code
    block, so the shared prefix is removed while relative indentation is kept.
    """
    lines = text.split("\n")
    widths = [
        len(line) - len(line.lstrip(" \t"))
        for line in lines
        if line.strip()
    ]
    if not widths:
        return text
    cut = min(widths)
    if cut == 0:
        return text
    return "\n".join(line[cut:] if line.strip() else line for line in lines)


_FENCE_LINE = re.compile(r"^(```+|~~~+)")
_LIST_ITEM = re.compile(r"^([-*+]|\d+[.)])\s")


def normalize_indentation(text: str) -> str:
    """Remove indentation that JSX nesting left behind.

    Content lifted out of <Tabs>/<TabItem> keeps the indentation it had inside
    the markup.  In Markdown four or more leading spaces mean a code block, so
    prose and fenced blocks are flushed left again.  Indentation that carries
    meaning — continuation lines inside a list — is preserved.
    """
    out: list[str] = []
    fence_marker: str | None = None
    fence_indent = 0
    list_indent: int | None = None

    for line in text.split("\n"):
        stripped = line.lstrip(" \t")
        indent = len(line) - len(stripped)

        if fence_marker is not None:
            if stripped.startswith(fence_marker):
                fence_marker = None
            out.append(line[min(indent, fence_indent):])
            continue

        m = _FENCE_LINE.match(stripped)
        if m:
            fence_marker = m.group(1)
            fence_indent = indent
            out.append(stripped)
            continue

        if not stripped:
            out.append("")
            continue

        if _LIST_ITEM.match(stripped):
            if list_indent is None or indent <= list_indent:
                list_indent = indent
            out.append(line if indent < 4 else stripped)
            continue

        if list_indent is not None and indent > list_indent:
            out.append(line)  # continuation of a list item
            continue

        list_indent = None
        out.append(stripped if indent >= 4 else line)

    return "\n".join(out)


def _bind_params(jsx: str, params: list[str], values: list[str]) -> str:
    """Substitute identifiers in a JSX body with the caller's arguments."""
    for idx, param in enumerate(params):
        value = values[idx] if idx < len(values) else "undefined"
        jsx = re.sub(rf"(?<![\w.]){re.escape(param)}(?![\w])", value, jsx)
    return jsx


_FENCE_RE = re.compile(r"^(?P<f>```+|~~~+)[^\n]*\n.*?^(?P=f)[ \t]*$", re.S | re.M)


def _mask_fences(text: str) -> tuple[str, list[str]]:
    store: list[str] = []

    def hide(m: re.Match) -> str:
        store.append(m.group(0))
        return f"\x00FENCE{len(store) - 1}\x00"

    return _FENCE_RE.sub(hide, text), store


def _unmask_fences(text: str, store: list[str]) -> str:
    for idx, original in enumerate(store):
        text = text.replace(f"\x00FENCE{idx}\x00", original)
    return text


def find_expressions(text: str) -> list[tuple[int, int, str]]:
    """Locate balanced ``{...}`` groups in JSX child positions."""
    spans: list[tuple[int, int, str]] = []
    i = 0
    n = len(text)
    while i < n:
        if text[i] != "{":
            i += 1
            continue
        depth = 0
        quote: str | None = None
        j = i
        while j < n:
            ch = text[j]
            if quote:
                if ch == "\\":
                    j += 2
                    continue
                if ch == quote:
                    quote = None
            elif ch in "\"'`":
                quote = ch
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        if j >= n or depth != 0:
            i += 1
            continue
        spans.append((i, j + 1, text[i + 1 : j]))
        i = j + 1
    return spans


class JsEvaluator:
    """Evaluates MDX interpolations with node, or gives up cleanly."""

    def __init__(self) -> None:
        self.available = True

    def evaluate(self, prelude: str, props: dict[str, str],
                 expressions: list[str]) -> list[str | None]:
        if not self.available or not expressions:
            return [None] * len(expressions)
        script = (
            f"const props = {json.dumps(props)};\n"
            f"{prelude}\n"
            f"const __exprs = {json.dumps(expressions)};\n"
            "const __out = __exprs.map(function (s) {\n"
            "  try {\n"
            "    const v = eval(s);\n"
            "    return (typeof v === 'string' || typeof v === 'number') ? String(v) : null;\n"
            "  } catch (e) { return null; }\n"
            "});\n"
            "process.stdout.write(JSON.stringify(__out));\n"
        )
        try:
            out = subprocess.run(
                ["node", "-e", script], capture_output=True, text=True,
                timeout=NODE_TIMEOUT,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            self.available = False
            return [None] * len(expressions)
        if out.returncode != 0 or not out.stdout:
            return [None] * len(expressions)
        try:
            values = json.loads(out.stdout)
        except json.JSONDecodeError:
            return [None] * len(expressions)
        if len(values) != len(expressions):
            return [None] * len(expressions)
        return values


# --------------------------------------------------------------------------
# Inline HTML used inside MDX
# --------------------------------------------------------------------------

_HTML_RULES: list[tuple[re.Pattern, str]] = [
    (re.compile(r"<h([1-6])>(.*?)</h\1>", re.S), None),   # handled specially
    (re.compile(r"<code>(.*?)</code>", re.S), r"`\1`"),
    (re.compile(r"<strong>(.*?)</strong>", re.S), r"**\1**"),
    (re.compile(r"<b>(.*?)</b>", re.S), r"**\1**"),
    (re.compile(r"<em>(.*?)</em>", re.S), r"*\1*"),
    (re.compile(r"<i>(.*?)</i>", re.S), r"*\1*"),
    (re.compile(r"<br\s*/?>"), "  \n"),
    (re.compile(r"</?p>"), "\n\n"),
]

_HEADING_RE = re.compile(r"<h([1-6])>(.*?)</h\1>", re.S)
_ANCHOR_RE = re.compile(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>', re.S)
# Docusaurus <Link to="/some/path">Label</Link>. The final path segment is the
# doc id, so emitting it as a .mdx link lets the normal link rewriter resolve it
# to a bundle concept, falling back to the docs site when it is not in-bundle.
_LINK_COMPONENT_RE = re.compile(r'<Link\s+to="([^"]+)"[^>]*>(.*?)</Link>', re.S)


def html_to_markdown(text: str) -> str:
    """Convert the small set of inline HTML tags the docs use."""
    masked, fences = _mask_fences(text)
    masked = _LINK_COMPONENT_RE.sub(
        lambda m: f"[{' '.join(m.group(2).split())}]"
                  f"({m.group(1).rstrip('/').rsplit('/', 1)[-1]}.mdx)",
        masked,
    )
    masked = _HEADING_RE.sub(
        lambda m: "\n\n" + "#" * int(m.group(1)) + " " + " ".join(m.group(2).split()) + "\n\n",
        masked,
    )
    masked = _ANCHOR_RE.sub(lambda m: f"[{m.group(2).strip()}]({m.group(1)})", masked)
    for pattern, repl in _HTML_RULES:
        if repl is None:
            continue
        masked = pattern.sub(repl, masked)
    return _unmask_fences(masked, fences)


# --------------------------------------------------------------------------
# Converter
# --------------------------------------------------------------------------

class MdxConverter:
    """Flattens one documentation tree's MDX into Markdown."""

    def __init__(self, repo_dir: Path, docs_dir: Path, javadoc_version: str | None):
        self.repo_dir = repo_dir
        self.docs_dir = docs_dir
        self.javadoc_version = javadoc_version or "latest"
        self.js = JsEvaluator()

    # -- partials ---------------------------------------------------------

    def _resolve_partial_path(self, source: str, from_file: Path) -> Path | None:
        if source.startswith(THEME_PREFIXES):
            return None
        if not source.endswith(PARTIAL_SUFFIXES):
            return None  # JS/TS React components cannot be inlined as Markdown
        if source.startswith("/"):
            candidate = self.repo_dir / source.lstrip("/")
        else:
            candidate = (from_file.parent / source).resolve()
        return candidate if candidate.is_file() else None

    def _inline_partial(self, path: Path, props: dict[str, str], depth: int) -> str:
        if depth > 4:
            return ""
        _, body = split_frontmatter(path.read_text("utf-8", errors="replace"))
        return "\n\n" + self._flatten(body, path, props, depth + 1).strip() + "\n\n"

    # -- components -------------------------------------------------------

    def _render_javadoc_link(self, attrs: dict[str, str], _children: str) -> str:
        package = attrs.get("packageName", "")
        path = attrs.get("path", "").strip("/")
        cls = attrs.get("className", "")
        if not package or not cls:
            return cls or ""
        url = (
            "https://javadoc.io/static/com.scalar-labs/"
            f"{package}/{self.javadoc_version}/{path}/{cls}.html"
        )
        return f"[`{cls}`]({url})"

    @staticmethod
    def _render_tabitem(attrs: dict[str, str], children: str) -> str:
        label = attrs.get("label") or attrs.get("value") or ""
        inner = dedent_block(children).strip("\n")
        return f"\n\n**{label}**\n\n{inner}\n\n" if label else f"\n\n{inner}\n\n"

    @staticmethod
    def _render_codeblock(attrs: dict[str, str], children: str) -> str:
        lang = attrs.get("language", "")
        code = children.strip()
        if code.startswith("{") and code.endswith("}"):
            code = code[1:-1].strip()
        if code.startswith("`") and code.endswith("`"):
            code = code.strip("`")
        code = code.strip("\n")
        fence = "```"
        while fence in code:
            fence += "`"
        return f"\n\n{fence}{lang}\n{code}\n{fence}\n\n"

    # -- driver -----------------------------------------------------------

    def _flatten(self, body: str, from_file: Path, props: dict[str, str] | None = None,
                 depth: int = 0) -> str:
        in_partial = props is not None
        props = props or {}
        # Code samples must be invisible to the import/export scanners: the docs
        # contain Java `import` statements and shell `export` lines.
        masked, fences = _mask_fences(body)
        imports = dict(IMPORT_RE.findall(masked))
        imports.pop("", None)
        masked = IMPORT_RE.sub("", masked)
        decls, masked = strip_export_prelude(masked)
        body = _unmask_fences(MDX_COMMENT_RE.sub("", masked), fences)

        # Local Markdown partials first: they carry their own prelude and props.
        for name, source in imports.items():
            path = self._resolve_partial_path(source, from_file)
            if path is None:
                continue
            body = _replace_component(
                body, name,
                lambda attrs, _children, p=path: self._inline_partial(p, attrs, depth),
            )

        jsx_defs = parse_prelude_jsx("\n".join(decls))
        js_prelude = js_safe_prelude(decls, jsx_defs)

        # Conditional rendering ({props.mode === 'x' && (<jsx/>)}) has to be
        # settled before and after component expansion: expanding a component
        # can expose further conditionals, and unwrapping a conditional exposes
        # the expressions inside it.
        for _ in range(3):
            before = body
            body = self._resolve_conditionals(body, js_prelude, props)
            body = self._expand_prelude_jsx(body, jsx_defs)
            if body == before:
                break
        body = self._evaluate_expressions(body, js_prelude, props)

        # MDX renders an undefined prop as nothing; a partial included without
        # the prop (which upstream sometimes does) must read the same way here.
        if in_partial:
            masked, fences = _mask_fences(body)
            body = _unmask_fences(re.sub(r"\{props\.\w+\}", "", masked), fences)

        body = _replace_component(body, "JavadocLink", self._render_javadoc_link)
        body = _replace_component(body, "CodeBlock", self._render_codeblock)
        body = _replace_component(body, "TabItem", self._render_tabitem)
        body = _replace_component(
            body, "Tabs", lambda a, c: "\n\n" + dedent_block(c).strip("\n") + "\n\n")
        body = _replace_component(
            body, "Admonition", lambda a, c: "\n\n" + dedent_block(c).strip("\n") + "\n\n")

        # React components that render navigation cards have no textual content;
        # the generated index.md listings replace them.
        for name in ("DocCardList", "CategoryGrid"):
            body = _replace_component(body, name, lambda a, c: "")

        # Components that could not be resolved to Markdown are dropped rather
        # than left as raw JSX, but only when they render nothing textual.
        for name in imports:
            if self._resolve_partial_path(imports[name], from_file) is None and \
                    imports[name].startswith(("/src/", "@site/")) and \
                    name not in ("JavadocLink",):
                body = _replace_component(body, name, lambda a, c: c)

        return html_to_markdown(body)

    @staticmethod
    def _expand_prelude_jsx(body: str, defs: dict[str, tuple[list[str], str]]) -> str:
        """Inline MDX-local components and JSX-returning helpers."""
        if not defs:
            return body
        for _ in range(6):
            before = body
            for name, (params, jsx) in defs.items():
                def render(attrs, children, _p=params, _j=jsx):
                    out = dedent_block(_j).replace("{children}", children)
                    for key, value in attrs.items():
                        out = re.sub(
                            rf"(?<![\w.]){re.escape(key)}(?![\w])",
                            json.dumps(value), out,
                        )
                    return out

                body = _replace_component(body, name, render)
                call = re.compile(rf"\{{\s*{re.escape(name)}\(([^()]*)\)\s*\}}")
                body = call.sub(
                    lambda m, _p=params, _j=jsx: _bind_params(
                        _j, _p, [a.strip() for a in m.group(1).split(",") if a.strip()]
                    ),
                    body,
                )
            if body == before:
                break
        return body

    _CONDITIONAL_RE = re.compile(r"(?s)^\s*(.+?)\s*&&\s*\(\s*(<.*)\s*\)\s*$")

    def _resolve_conditionals(self, body: str, prelude: str,
                              props: dict[str, str]) -> str:
        """Unwrap ``{cond && (<jsx/>)}`` blocks by evaluating the condition.

        A truthy condition keeps the JSX children in place; a falsy one removes
        the block, matching what Docusaurus renders for these props.  When the
        condition cannot be evaluated the block is left untouched.
        """
        masked, fences = _mask_fences(body)
        found = []
        for start, end, expr in find_expressions(masked):
            m = self._CONDITIONAL_RE.match(expr)
            if m:
                found.append((start, end, m.group(1), m.group(2)))
        if not found:
            return body

        verdicts = self.js.evaluate(
            prelude, props, [f"String(Boolean({cond}))" for _, _, cond, _ in found]
        )
        out = masked
        for (start, end, _cond, jsx), verdict in zip(reversed(found), reversed(verdicts)):
            if verdict == "true":
                out = out[:start] + "\n" + dedent_block(jsx).strip("\n") + "\n" + out[end:]
            elif verdict == "false":
                out = out[:start] + out[end:]
        return _unmask_fences(out, fences)

    def _evaluate_expressions(self, body: str, prelude: str,
                              props: dict[str, str]) -> str:
        """Resolve {...} interpolations; leave anything unresolvable untouched."""
        if not prelude and not props:
            return body

        masked, fences = _mask_fences(body)
        spans = find_expressions(masked)
        spans = [s for s in spans if s[2].strip()]
        if not spans:
            return body

        values = self.js.evaluate(prelude, props, [s[2] for s in spans])
        out = masked
        for (start, end, _expr), value in zip(reversed(spans), reversed(values)):
            if value is None:
                continue
            out = out[:start] + value + out[end:]
        return _unmask_fences(out, fences)

    def convert(self, path: Path) -> Conversion:
        raw = path.read_text("utf-8", errors="replace")
        frontmatter, body = split_frontmatter(raw)
        body = self._flatten(body, path)

        stripped, _ = _mask_fences(body)
        stripped = re.sub(r"`[^`\n]*`", "", stripped)
        unresolved = {
            m.group(1) for m in re.finditer(r"</?([A-Z][A-Za-z0-9]*)[\s/>]", stripped)
        }
        # Authoring notes left in HTML comments are not documentation content.
        masked, fences = _mask_fences(body)
        body = _unmask_fences(re.sub(r"<!--.*?-->", "", masked, flags=re.S), fences)

        body = normalize_indentation(body)
        body = re.sub(r"[ \t]+$", "", body, flags=re.M)
        body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"
        return Conversion(frontmatter=frontmatter, body=body, unresolved=unresolved)


# --------------------------------------------------------------------------
# Titles, summaries, links
# --------------------------------------------------------------------------

_ADMONITION = re.compile(r"^:::.*$", re.M)
_HTML_TAG = re.compile(r"<[^>]+>")
_MD_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
_MD_EMPH = re.compile(r"[*_`]{1,3}")


def extract_title(body: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+?)\s*$", body, re.M)
    if m:
        return _MD_EMPH.sub("", _MD_LINK.sub(r"\1", m.group(1))).strip()
    return fallback


def extract_description(body: str, limit: int = 240) -> str:
    """First real sentence of the page, flattened to one line."""
    text = re.sub(r"^#.*$", "", body, flags=re.M)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = _ADMONITION.sub("", text)
    for block in re.split(r"\n\s*\n", text):
        block = block.strip()
        if not block or block[0] in "|>-*:!<":
            continue
        block = _MD_LINK.sub(r"\1", block)
        block = _HTML_TAG.sub("", block)
        block = _MD_EMPH.sub("", block)
        block = " ".join(block.split())
        if len(block) < 20:
            continue
        if len(block) > limit:
            cut = block[:limit]
            block = (cut[: cut.rfind(" ")] + "...") if " " in cut else cut
        return block
    return ""


_LINK_TARGET = re.compile(r"(\]\()([^)\s]+)(\s+\"[^\"]*\")?(\))")


def rewrite_links(body: str, to_md: dict[str, str], site_base: str, doc_dir: str) -> str:
    """Point in-bundle links at .md siblings and absolutise everything else.

    ``to_md`` maps a version-relative doc id to its bundle-relative path so that
    upstream ``foo.mdx`` links become OKF concept links.
    """

    def fix(m: re.Match) -> str:
        target = m.group(2)
        title = m.group(3) or ""
        if target.startswith(("http://", "https://", "#", "mailto:")):
            return m.group(0)

        anchor = ""
        if "#" in target:
            target, anchor = target.split("#", 1)
            anchor = "#" + anchor
        if not target:
            return m.group(0)

        if target.endswith((".mdx", ".md")):
            base = target.rsplit(".", 1)[0]
            resolved = _normalise(doc_dir, base)
            if resolved in to_md:
                rel = _relative(doc_dir, to_md[resolved])
                return f"{m.group(1)}{rel}{anchor}{title}{m.group(4)}"
            return f"{m.group(1)}{site_base}/{resolved}/{anchor}{title}{m.group(4)}"

        # Images and other static assets stay on the docs site.
        resolved = _normalise(doc_dir, target)
        return f"{m.group(1)}{site_base}/{resolved}{anchor}{title}{m.group(4)}"

    return _LINK_TARGET.sub(fix, body)


def _normalise(doc_dir: str, target: str) -> str:
    parts = [p for p in (doc_dir.split("/") if doc_dir else []) if p]
    for piece in target.split("/"):
        if piece in ("", "."):
            continue
        if piece == "..":
            if parts:
                parts.pop()
        else:
            parts.append(piece)
    return "/".join(parts)


def _relative(from_dir: str, to_path: str) -> str:
    src = [p for p in from_dir.split("/") if p]
    dst = to_path.split("/")
    name = dst.pop()
    common = 0
    while common < len(src) and common < len(dst) and src[common] == dst[common]:
        common += 1
    up = [".."] * (len(src) - common)
    down = dst[common:]
    rel = "/".join(up + down + [name])
    return rel if rel.startswith("..") else "./" + rel
