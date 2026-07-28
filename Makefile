PYTHON ?= python3

.PHONY: build update validate offline clean help

help:
	@echo "make build     - sync upstream docs and rebuild the whole bundle"
	@echo "make update    - add versions that are not in the bundle yet (+ refresh latest)"
	@echo "make offline   - rebuild from the cached clones, no network"
	@echo "make validate  - check OKF v0.2 conformance"
	@echo "make clean     - remove the upstream clone cache"

build:
	$(PYTHON) tools/okf_build.py

update:
	$(PYTHON) tools/okf_build.py --only-new

offline:
	$(PYTHON) tools/okf_build.py --offline

validate:
	$(PYTHON) tools/okf_validate.py

clean:
	rm -rf .cache
