---
type: Documentation Section
title: ScalarDL 3.12 — Scalar Kubernetes
description: Directory listing for the `scalar-kubernetes` section of the ScalarDL 3.12 documentation.
resource: https://scalardl.scalar-labs.com/docs/3.12/scalar-kubernetes/
tags:
- scalardl
- v3.12
- index
status: stable
product: scalardl
version: '3.12'
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:51:01Z'
---

# Scalar Kubernetes

ScalarDL 3.12 documentation under `scalar-kubernetes/`.

## Subsections

- [alerts](./alerts/index.md)

## Concepts

- [(Deprecated) Guidelines for creating an EKS cluster for ScalarDB Server](./CreateEKSClusterForScalarDB.md) — ScalarDB Server is now deprecated. Please use ScalarDB Cluster instead.
- [[Deprecated] Deploy ScalarDB Server on Azure Kubernetes Service (AKS)](./ManualDeploymentGuideScalarDBServerOnAKS.md) — This guide explains how to deploy ScalarDB Server on Azure Kubernetes Service (AKS).
- [Back up a NoSQL database in a Kubernetes environment](./BackupNoSQL.md) — This guide explains how to create a transactionally consistent backup of managed databases that ScalarDB or ScalarDL uses in a Kubernetes environment. Please note that, when using a NoSQL database or multiple databases, you must pause...
- [Back up an RDB in a Kubernetes environment](./BackupRDB.md) — This guide explains how to create a backup of a single relational database (RDB) that ScalarDB or ScalarDL uses in a Kubernetes environment. Please note that this guide assumes that you are using a managed database from a cloud services...
- [Back up and restore ScalarDB or ScalarDL data in a Kubernetes environment](./BackupRestoreGuide.md) — This guide explains how to backup and restore ScalarDB or ScalarDL data in a Kubernetes environment. Please note that this guide assumes that you are using a managed database from a cloud services provider as the backend database for...
- [Collecting logs from Scalar products on a Kubernetes cluster](./K8sLogCollectionGuide.md) — This document explains how to deploy Grafana Loki and Promtail on Kubernetes with Helm. After following this document, you can collect logs of Scalar products on your Kubernetes environment.
- [Components to Regularly Check When Running in a Kubernetes Environment](./RegularCheck.md) — Most of the components deployed by manual deployment guides are self-healing with the help of the managed Kubernetes services and Kubernetes self-healing capability. There are also configured alerts that occur when some unexpected behavior...
- [Configure Network Peering for ScalarDL Auditor Mode](./NetworkPeeringForScalarDLAuditor.md) — This document explains how to connect multiple private networks for ScalarDL Auditor mode to perform network peering. For ScalarDL Auditor mode to work properly, you must connect ScalarDL Ledger to ScalarDL Auditor.
- [Create a bastion server](./CreateBastionServer.md) — This document explains how to create a bastion server and install some tools for the deployment of Scalar products.
- [Deploy ScalarDB Cluster on Amazon Elastic Kubernetes Service (EKS)](./ManualDeploymentGuideScalarDBClusterOnEKS.md) — This guide explains how to deploy ScalarDB Cluster on Amazon Elastic Kubernetes Service (EKS).
- [Deploy ScalarDB Server on Amazon Elastic Kubernetes Service (EKS)](./ManualDeploymentGuideScalarDBServerOnEKS.md) — This guide explains how to deploy ScalarDB Server on Amazon Elastic Kubernetes Service (EKS).
- [Deploy ScalarDL Ledger and ScalarDL Auditor on Amazon Elastic Kubernetes Service (EKS)](./ManualDeploymentGuideScalarDLAuditorOnEKS.md) — This guide explains how to deploy ScalarDL Ledger and ScalarDL Auditor on Amazon Elastic Kubernetes Service (EKS).
- [Deploy ScalarDL Ledger and ScalarDL Auditor on Azure Kubernetes Service (AKS)](./ManualDeploymentGuideScalarDLAuditorOnAKS.md) — This guide explains how to deploy ScalarDL Ledger and ScalarDL Auditor on Azure Kubernetes Service (AKS).
- [Deploy ScalarDL Ledger on Amazon Elastic Kubernetes Service (EKS)](./ManualDeploymentGuideScalarDLOnEKS.md) — This document explains how to deploy ScalarDL Ledger on Amazon Elastic Kubernetes Service (EKS).
- [Deploy ScalarDL Ledger on Azure Kubernetes Service (AKS)](./ManualDeploymentGuideScalarDLOnAKS.md) — This document explains how to deploy ScalarDL Ledger on Azure Kubernetes Service (AKS).
- [Guidelines for creating an AKS cluster for Scalar products](./CreateAKSClusterForScalarProducts.md) — To create an Azure Kubernetes Service (AKS) cluster for Scalar products, refer to the following:
- [Guidelines for creating an AKS cluster for ScalarDB Server](./CreateAKSClusterForScalarDB.md) — This document explains the requirements and recommendations for creating an Azure Kubernetes Service (AKS) cluster for ScalarDB Server deployment. For details on how to deploy ScalarDB Server on an AKS cluster, see Deploy ScalarDB Server...
- [Guidelines for creating an AKS cluster for ScalarDL Ledger](./CreateAKSClusterForScalarDL.md) — This document explains the requirements and recommendations for creating an Azure Kubernetes Service (AKS) cluster for ScalarDL Ledger deployment. For details on how to deploy ScalarDL Ledger on an AKS cluster, see Deploy ScalarDL Ledger...
- [Guidelines for creating an AKS cluster for ScalarDL Ledger and ScalarDL Auditor](./CreateAKSClusterForScalarDLAuditor.md) — This document explains the requirements and recommendations for creating an Azure Kubernetes Service (AKS) cluster for ScalarDL Ledger and ScalarDL Auditor deployment. For details on how to deploy ScalarDL Ledger and ScalarDL Auditor on an...
- [Guidelines for creating an Amazon EKS cluster for Scalar products](./CreateEKSClusterForScalarProducts.md) — To create an Amazon Elastic Kubernetes Service (EKS) cluster for Scalar products, refer to the following:
- [Guidelines for creating an EKS cluster for ScalarDB Cluster](./CreateEKSClusterForScalarDBCluster.md) — This document explains the requirements and recommendations for creating an Amazon Elastic Kubernetes Service (EKS) cluster for ScalarDB Cluster deployment. For details on how to deploy ScalarDB Cluster on an EKS cluster, see Deploy...
- [Guidelines for creating an EKS cluster for ScalarDL Ledger](./CreateEKSClusterForScalarDL.md) — This document explains the requirements and recommendations for creating an Amazon Elastic Kubernetes Service (EKS) cluster for ScalarDL Ledger deployment. For details on how to deploy ScalarDL Ledger on an EKS cluster, see Deploy ScalarDL...
- [Guidelines for creating an EKS cluster for ScalarDL Ledger and ScalarDL Auditor](./CreateEKSClusterForScalarDLAuditor.md) — This document explains the requirements and recommendations for creating an Amazon Elastic Kubernetes Service (EKS) cluster for ScalarDL Ledger and ScalarDL Auditor deployment. For details on how to deploy ScalarDL Ledger and ScalarDL...
- [How to Create Private Key and Certificate Files for TLS Connections in Scalar Products](./HowToCreateKeyAndCertificateFiles.md) — This guide explains how to create private key and certificate files for TLS connections in ScalarDB Cluster and ScalarDL. When you enable the TLS feature, you must prepare private key and certificate files.
- [How to get the container images of Scalar products](./HowToGetContainerImages.md) — You can get the container images of Scalar products in several ways. Please choose one of the following methods.
- [How to install Scalar products through AWS Marketplace](./AwsMarketplaceGuide.md) — Scalar products (ScalarDB, ScalarDL, and their tools) are available in the AWS Marketplace as container images. This guide explains how to install Scalar products through the AWS Marketplace.
- [How to Scale ScalarDB Cluster](./HowToScaleScalarDB.md) — This guide explains how to scale ScalarDB Cluster. The contents of this guide assume that you used Scalar Helm Chart to deploy ScalarDB Cluster, which is the recommended way.
- [How to Scale ScalarDL](./HowToScaleScalarDL.md) — This guide explains how to scale ScalarDL. The contents of this guide assume that you used Scalar Helm Chart to deploy ScalarDL, which is the recommended way.
- [How to Upgrade ScalarDB](./HowToUpgradeScalarDB.md) — This guide explains how to upgrade to a newer version of ScalarDB.
- [How to Upgrade ScalarDL](./HowToUpgradeScalarDL.md) — This guide explains how to upgrade to a newer version of ScalarDL.
- [How to use the container images](./HowToUseContainerImages.md) — You can pull the container images from the public container repository. You must configure the license key and the certificate in your .properties file if you use the container images.
- [Make ScalarDB or ScalarDL deployed in a Kubernetes cluster environment available from applications](./AccessScalarProducts.md) — This document explains how to make ScalarDB or ScalarDL deployed in a Kubernetes cluster environment available from applications. To make ScalarDB or ScalarDL available from applications, you can use Scalar Envoy via a Kubernetes service...
- [Monitoring Scalar products on a Kubernetes cluster](./K8sMonitorGuide.md) — This document explains how to deploy Prometheus Operator on Kubernetes with Helm. After following this document, you can use Prometheus, Alertmanager, and Grafana for monitoring Scalar products on your Kubernetes environment.
- [Production checklist for Scalar products](./ProductionChecklistForScalarProducts.md) — To make your deployment ready for production, refer to the following:
- [Production checklist for ScalarDB Cluster](./ProductionChecklistForScalarDBCluster.md) — This checklist provides recommendations when deploying ScalarDB Cluster in a production environment.
- [Production checklist for ScalarDL Auditor](./ProductionChecklistForScalarDLAuditor.md) — This checklist provides recommendations when deploying ScalarDL Auditor in a production environment.
- [Production checklist for ScalarDL Ledger](./ProductionChecklistForScalarDLLedger.md) — This checklist provides recommendations when deploying ScalarDL Ledger in a production environment.
- [Restore databases in a Kubernetes environment](./RestoreDatabase.md) — This guide explains how to restore databases that ScalarDB or ScalarDL uses in a Kubernetes environment. Please note that this guide assumes that you are using a managed database from a cloud services provider as the backend database for...
- [Set up a database for ScalarDB/ScalarDL deployment](./SetupDatabase.md) — This guide explains how to set up a database for ScalarDB/ScalarDL deployment on cloud services.
- [Set up a database for ScalarDB/ScalarDL deployment on AWS](./SetupDatabaseForAWS.md) — This guide explains how to set up a database for ScalarDB/ScalarDL deployment on AWS.
- [Set up a database for ScalarDB/ScalarDL deployment on Azure](./SetupDatabaseForAzure.md) — This guide explains how to set up a database for ScalarDB/ScalarDL deployment on Azure.
