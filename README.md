# Integrated Data Management and Analytics System

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Key Components Implementation](#key-components-implementation)
- [Usage](#usage)
- [Contributing](#contributing)

## Project Overview

The **Integrated Data Management and Analytics System** is designed to integrate data from multiple sources, process it through robust ETL pipelines, and provide actionable insights via advanced analytics and reporting tools. This system supports predictive analytics and real-time decision-making, aligning with Brex's goal to empower teams with data-driven insights.

## Technologies Used

- **Data Ingestion and Streaming:** Apache Kafka, AWS Kinesis
- **Data Transformation:** DBT, Python
- **Data Warehousing:** Snowflake
- **Workflow Orchestration:** Apache Airflow
- **Machine Learning:** Python (scikit-learn, TensorFlow)
- **BI Tools:** Looker, Tableau
- **Programming:** Python, SQL
- **Others:** Git, Docker, AWS services

## Setup Instructions

### Prerequisites

- **Git**
- **Docker & Docker Compose**
- **Python 3.8+**
- **Snowflake Account**
- **Apache Kafka or AWS Kinesis Account**
- **Apache Airflow**
- **DBT Account**
- **BI Tool Account**

### Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/junelus/integrated-data-management.git
    cd integrated-data-management
    ```

2. **Set Up Environment Variables:**
    Create a `.env` file and add necessary environment variables.

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Start Services:**
    ```bash
    docker-compose up -d
    ```

5. **Initialize DBT:**
    ```bash
    cd dbt_project
    dbt init
    dbt run
    ```

6. **Set Up Airflow:**
    Access Airflow UI via `http://localhost:8080`.

## Key Components Implementation

Detailed implementation steps are provided in the [Key Components Implementation](#key-components-implementation) section.

## Usage

- **Data Ingestion:**
    Run the Kafka producer scripts to start ingesting data.
  
- **ETL Pipeline:**
    Access Apache Airflow UI to monitor and trigger ETL jobs.

- **Machine Learning:**
    Train models using scripts in the `machine_learning/` directory.

- **BI Reporting:**
    Access dashboards via Looker or Tableau.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.
