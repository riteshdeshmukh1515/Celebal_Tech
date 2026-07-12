# Assignment No. 4

# Azure Cloud Fundamentals and Data Pipeline Implementation using Azure Data Factory (ADF)

---

## Student Information

**Assignment:** Assignment No. 4
**Title:** Azure Cloud Fundamentals and Data Pipeline Implementation using Azure Data Factory (ADF)

---

# Objective

The objective of this assignment is to understand Microsoft Azure cloud fundamentals and implement a complete end-to-end data pipeline using Azure Storage Account and Azure Data Factory (ADF). The project demonstrates how to store data in Azure Blob Storage, validate file metadata, copy data between Blob containers, monitor pipeline execution, and configure Azure IAM roles for secure access.

---

# Problem Statement

Build a complete data pipeline that reads a CSV file from Azure Blob Storage and processes it using Azure Data Factory.

### Requirements

* Create a Resource Group.
* Create an Azure Storage Account.
* Create Blob Containers.
* Upload a CSV dataset.
* Create Azure Data Factory.
* Configure Linked Service.
* Create Source and Destination Datasets.
* Retrieve file information using Get Metadata.
* Copy the CSV file using Copy Data activity.
* Monitor the pipeline execution.
* Configure IAM roles between Azure Data Factory and Azure Storage.
* Verify successful execution.

---

# Azure Services Used

* Microsoft Azure Portal
* Azure Resource Group
* Azure Storage Account
* Azure Blob Storage
* Azure Data Factory (ADF)
* Azure Identity and Access Management (IAM)

---

# Project Architecture

```text
                  Sample-Superstore.csv
                        │
                        ▼
        Azure Blob Storage (Input Container)
                        │
                 Linked Service (ADF)
                        │
                        ▼
             Azure Data Factory Pipeline
                        │
        ┌───────────────┴───────────────┐
        │                               │
        ▼                               ▼
 Get Metadata Activity          Copy Data Activity
        │                               │
        └───────────────┬───────────────┘
                        │
                        ▼
     Azure Blob Storage (Destination Container)
                        │
                        ▼
              Sample-Superstore_Copy.csv
```

---

# Project Workflow

1. Login to Azure Portal.
2. Create a Resource Group.
3. Create an Azure Storage Account.
4. Create Blob Containers (`input` and `destination`).
5. Upload the Superstore CSV dataset into the **input** container.
6. Create Azure Data Factory.
7. Launch Azure Data Factory Studio.
8. Create a Linked Service for Azure Blob Storage.
9. Create Source and Destination Datasets.
10. Create a pipeline.
11. Add Get Metadata activity.
12. Add Copy Data activity.
13. Validate the pipeline.
14. Publish the pipeline.
15. Execute the pipeline using Debug/Trigger.
16. Monitor the execution.
17. Verify the copied file in the destination container.
18. Configure IAM roles.

---

# Azure Resources Created

## 1. Resource Group

**Purpose**

A Resource Group is a logical container that stores all Azure resources used in this project.

---

## 2. Storage Account

**Purpose**

The Storage Account stores Blob containers and dataset files.

### Blob Containers

### Input Container

Stores the original CSV dataset.

```text
input/
    Sample-Superstore.csv
```

### Destination Container

Stores the copied CSV file after pipeline execution.

```text
destination/
    Sample-Superstore_Copy.csv
```

---

## 3. Azure Data Factory

Azure Data Factory is the cloud-based ETL service used to build and execute the pipeline.

Components created:

* Linked Service
* Source Dataset
* Destination Dataset
* Pipeline
* Get Metadata Activity
* Copy Data Activity

---

# Linked Service

## Azure Blob Storage Linked Service

**Purpose**

The Linked Service establishes a secure connection between Azure Data Factory and Azure Blob Storage.

### Authentication Method

* Account Key

---

# Datasets

## Source Dataset

| Property     | Value              |
| ------------ | ------------------ |
| Dataset Name | DS_Source          |
| Storage Type | Azure Blob Storage |
| Container    | input              |
| File         | Sample-Superstore.csv     |
| Format       | Delimited Text     |

---

## Destination Dataset

| Property     | Value               |
| ------------ | ------------------- |
| Dataset Name | DS_Destination      |
| Storage Type | Azure Blob Storage  |
| Container    | destination         |
| File         | Superstore_Copy.csv |
| Format       | Delimited Text      |

---

# Pipeline Design

Pipeline Name

```text
Pipeline_CopyData
```

Pipeline Flow

```text
Input Blob Container
        │
        ▼
Get Metadata
        │
        ▼
Copy Data
        │
        ▼
Destination Blob Container
```

---

# Activities Used

## 1. Get Metadata Activity

### Purpose

Retrieves information about the source file before processing.

### Metadata Retrieved

* Exists
* Size
* Last Modified

### Sample Output

```text
Exists : True

Size : 2.4 MB

Last Modified :
12 July 2026
```

---

## 2. Copy Data Activity

### Purpose

Copies the CSV file from the **input** container to the **destination** container.

### Source

```text
input/Sample-Superstore.csv
```

### Destination

```text
destination/Sample-Superstore_Copy.csv
```

---

# IAM Role Configuration

To enable secure communication between Azure Data Factory and Azure Storage, the following roles were configured.

| Role                          | Purpose                                                          |
| ----------------------------- | ---------------------------------------------------------------- |
| Reader                        | Allows read access to Azure resources.                           |
| Contributor                   | Allows management of Azure resources (excluding access control). |
| Storage Blob Data Contributor | Allows Azure Data Factory to read and write Blob Storage data.   |

---

# Pipeline Validation

The pipeline was validated before execution.

**Validation Result**

```text
Your pipeline has been validated.
No errors were found.
```

---

# Pipeline Execution

The pipeline was executed using **Debug** and **Trigger Now**.

### Execution Status

```text
Succeeded
```

### Activities Completed

* Get Metadata – Succeeded
* Copy Data – Succeeded

---

# Monitoring

Pipeline execution was monitored using the **Monitor** section of Azure Data Factory.

The Monitor page provides:

* Pipeline Status
* Activity Status
* Start Time
* End Time
* Execution Duration
* Data Read
* Data Written

---

# Output Verification

After successful execution, the destination container contained the copied CSV file.

```text
destination/
    Sample-Superstore_Copy.csv
```

The metadata validation confirmed:

* Source file exists.
* File size retrieved successfully.
* Last modified timestamp retrieved successfully.
* Data copied successfully to the destination container.

---

# Screenshots Included

* Azure Portal Dashboard
* Resource Group
* Storage Account
* Input Blob Container
* Destination Blob Container
* Uploaded CSV File
* Azure Data Factory Overview
* Linked Service
* Source Dataset
* Destination Dataset
* Pipeline Design
* Get Metadata Activity
* Copy Data Activity
* Pipeline Validation
* Pipeline Execution (Succeeded)
* Monitor Page
* Output File in Destination Container
* IAM Role Assignments

---

# Learning Outcomes

Through this assignment, the following concepts were learned:

* Azure Cloud Fundamentals
* Azure Resource Management
* Azure Blob Storage
* Azure Data Factory
* Linked Services
* Datasets
* Get Metadata Activity
* Copy Data Activity
* Pipeline Validation
* Pipeline Monitoring
* Azure IAM and RBAC
* End-to-End Cloud Data Pipeline Development

---

# Conclusion

This assignment successfully demonstrated the implementation of an end-to-end Azure data pipeline using Azure Blob Storage and Azure Data Factory. The CSV dataset stored in the **input** Blob container was validated using the **Get Metadata** activity and copied to the **destination** Blob container using the **Copy Data** activity. The pipeline was validated, published, executed successfully, and monitored through Azure Data Factory. Appropriate IAM roles were configured to provide secure access between Azure Data Factory and Azure Storage. This assignment provided practical experience with Azure cloud services, storage management, data movement, and cloud-based ETL pipeline development.
