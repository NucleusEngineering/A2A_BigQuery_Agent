# Project Setup Guide

This document provides a comprehensive guide to set up and run the project.

## 1. Prerequisites

Before you begin, ensure you have the following tools installed:
-   **Python 3.12+**
-   **[Google Cloud SDK](https://cloud.google.com/sdk/docs/install)** to manage your Google Cloud resources.

## 2. Initial Setup

**Clone the Repository**:
```bash
git clone https://github.com/NucleusEngineering/A2A_BigQuery_Agent.git
cd A2A_BigQuery_Agent/kitchen_agent
```

## 3. Google Cloud Infrastructure & Environment Variable Setup

To start testing the agent this project requires specific GCP infrastructure setup as well as correctly set environment variables.

1.  **Configure Environment Variables**:
    *   Copy `dotenv` to `.env`:
        ```bash
        cp dotenv .env
        ```
    *   Edit the newly created `.env` file and fill in your `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION`. The other variables should stay unchanged.

2.  **Authenticate Google Cloud CLI**:
    *   Log in to your Google Cloud account:
        ```bash
        gcloud auth application-default login
        ```
    *   Set the active Google Cloud project:
        ```bash
        gcloud config set project <your-gcp-project-id>
        ```

3.  **Create and fill a BigQuery table**:
    *   This command will create a BigQuery datasest & table in your set project & location.
    *   Afterwards this table will be filled with the necessary data for the agent.
    *   Run this command:
        ```bash
        bq --location=$GOOGLE_CLOUD_LOCATION mk --dataset $GOOGLE_CLOUD_PROJECT:kitchen_inventory
        bq mk --location=$GOOGLE_CLOUD_LOCATION --table $GOOGLE_CLOUD_PROJECT:kitchen_inventory.fruits name:STRING,quantity:INTEGER
        ```
    *   Run this command to populate the table (make sure you are in the `kitchen_inventory` directory):
        ```bash
        bq load --source_format=CSV \
        $GOOGLE_CLOUD_PROJECT:kitchen_inventory.fruits \
        ./fruits_data.csv \
        name:STRING,quantity:INTEGER
        ```

4.  **Create virtual environment & necessary requirements download**:
    *   Navigate back to the root directory (A2A_BigQuery_Agent):
        ```bash
        cd ..
        ```
    *   Create a virtual environment & activate it:
        ```bash
        uv venv --python 3.12
        source .venv/bin/activate
        ```
    *   Install the necessary libraries:
        ```bash
        pip install -r requirements.txt
        ```

---
## Great! Your setup is complete.
Go to [TUTORIAL.md](./TUTORIAL.md) to run the agent.
        
        
