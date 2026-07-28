---
type: Deployment Guide
title: Ledger Alerts
description: This is the most critical alert and indicates that an Ledger cluster is not able to process requests. This alert should be handled with the highest priority.
resource: https://scalardl.scalar-labs.com/docs/latest/scalar-kubernetes/alerts/Ledger/
tags:
- scalardl
- v3.13
- phase:operate
- edition:enterprise
status: stable
product: scalardl
product_title: ScalarDL
version: '3.13'
patch_version: 3.13.0
doc_id: scalar-kubernetes/alerts/Ledger
lifecycle_phase: operate
editions:
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:30Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/eecc7f890d648a2f4ff33d60e5a96d57a1aa74d4/docs/scalar-kubernetes/alerts/Ledger.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-07-24T17:50:50Z'
---

# Ledger Alerts

## LedgerClusterDown

This is the most critical alert and indicates that an Ledger cluster is not able to process requests. This alert should be handled with the highest priority.

### Example Alert

#### Firing

```
[FIRING:1] LedgerClusterDown - critical
Alert: Ledger cluster is down - critical
 Description: Ledger cluster is down, no resquest can be process.
 Details:
  • alertname: LedgerClusterDown
  • deployment: prod-scalardl-ledger
```

#### Resolved

```
[RESOLVED] LedgerClusterDown - critical
Alert: Ledger cluster is down - critical
 Description: Ledger cluster is down, no resquest can be process.
 Details:
  • alertname: LedgerClusterDown
  • deployment: prod-scalardl-ledger
```

### Action Needed

* Check the number of replicas set `kubectl get deployments. prod-scalardl-ledger`
* Check the number of replicas set `kubectl describe deployments. prod-scalardl-ledger`
* Check nodes statuses with `kubectl get node -o wide`
* Check the log server to pinpoint the root cause of a failure with kubernetes logs on the monitor server `/log/kubernetes/<year>/<month>-<day>/kube.log`
* Check a cloud provider to see if there is any known issue. For example, you can check statues [here](https://status.azure.com/en-us/status) in Azure.

## LedgerClusterDegraded

This alert lets you know if a kubernetes cluster cannot start ledger pods, which means that the cluster does not have enough resource or lost of one or many kubernetes nodes to run the deployment.

### Example Alert

#### Firing

```
[FIRING:1] LedgerClusterDegraded - warning
Alert: Ledger cluster is running in a degraded mode - warning
 Description: Ledger cluster is running in a degraded mode, some of the Ledger pods are not healthy.
 Details:
  • alertname: LedgerClusterDegraded
  • deployment: prod-scalardl-ledger
```

#### Resolved

```
[RESOLVED] LedgerClusterDegraded - warning
Alert: Ledger cluster is running in a degraded mode - warning
 Description: Ledger cluster is running in a degraded mode, some of the Ledger pods are not healthy.
 Details:
  • alertname: LedgerClusterDegraded
  • deployment: prod-scalardl-ledger
```

### Action Needed

* Check the log server to pinpoint the root cause of a failure with kubernetes logs on the monitor server `/log/kubernetes/<year>/<month>-<day>/kube.log`
* Check kubernetes deployment with `kubectl describe deployments prod-scalardl-ledger`
* Check replica set with `kubectl get replicasets.apps`
* Check nodes statuses with `kubectl get node -o wide`
* Check a cloud provider to see if there is any known issue. For example, you can check statues [here](https://status.azure.com/en-us/status) in Azure.

## LedgerPodsPending

This alert lets you know if a kubernetes cluster cannot start ledger pods, which means that the cluster does not have the enough resource.

### Example Alert

#### Firing

```
[FIRING:1] LedgerPodsPending - warning
Alert: Pod prod-scalardl-ledger-xxxx-yyyy in namespace default in pending status - warning
 Description: Pod prod-scalardl-ledger-xxxx-yyyy in namespace default has been in pending status for more than 1 minute.
 Details:
  • alertname: LedgerPodsPending
  • deployment: prod-scalardl-ledger
```

#### Resolved

```
[RESOLVED:1] LedgerPodsPending - warning
Alert: Pod prod-scalardl-ledger-xxxx-yyyy in namespace default in pending status - warning
 Description: Pod prod-scalardl-ledger-xxxx-yyyy in namespace default has been in pending status for more than 1 minute.
 Details:
  • alertname: LedgerPodsPending
  • deployment: prod-scalardl-ledger
```

### Action Needed

* Check log server to pinpoint root cause of failure with the kubernetes logs on the monitor server `/log/kubernetes/<year>/<month>-<day>/kube.log`
* Check the kubernetes deployment with `kubectl describe pod prod-scalardl-ledger-xxxx-yyyy`

## LedgerPodsError

This alert lets you know if a kubernetes cluster cannot start ledger pods for one of the following reasons:

* CrashLoopBackOff
* CreateContainerConfigError
* CreateContainerError
* ErrImagePull
* ImagePullBackOff
* InvalidImageName

### Example Alert

#### Firing

```
[FIRING:1] LedgerPodsError - warning
Alert: Pod prod-scalardl-ledger-xxxx-yyyy in namespace default has an error status - warning
 Description: Pod prod-scalardl-ledger-xxxx-yyyy in namespace default has been in pending status for more than 1 minutes.
 Details:
  • alertname: LedgerPodsError
  • deployment: prod-scalardl-ledger
```

#### Resolved

```
[RESOLVED:1] LedgerPodsError - warning
Alert: Pod prod-scalardl-ledger-xxxx-yyyy in namespace default has an error status - warning
 Description: Pod prod-scalardl-ledger-xxxx-yyyy in namespace default has been in pending status for more than 1 minutes.
 Details:
  • alertname: LedgerPodsError
  • deployment: prod-scalardl-ledger
```

### Action Needed

* Check the kubernetes deployment with `kubectl describe pod prod-scalardl-ledger-xxxx-yyyy`
* Check log server to pinpoint root cause of failure with the kubernetes logs on the monitor server `/log/kubernetes/<year>/<month>-<day>/kube.log`
