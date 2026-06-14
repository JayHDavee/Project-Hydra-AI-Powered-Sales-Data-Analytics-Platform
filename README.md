# Project Hydra: AI-Powered Data Analytics Platform

## Overview

Project Hydra is an AI-powered data analytics platform that enables users to upload datasets, store them in PostgreSQL, and query them using natural language. The system leverages FastAPI for backend services, PostgreSQL for data storage, SQLAlchemy for database connectivity, and Google's Gemini API for Text-to-SQL generation.

The goal of this project is to bridge the gap between raw business data and business insights by allowing users to interact with databases using plain English instead of writing SQL queries manually.

---

## Features Implemented

### 1. Data Ingestion Pipeline

* Upload CSV files through FastAPI.
* Automatically process datasets using Pandas.
* Store uploaded datasets into PostgreSQL tables.
* Support multiple datasets.

### 2. Dataset Management

* View all available datasets.
* Preview dataset contents.
* Generate dataset summaries.
* Discover database schema dynamically.

### 3. PostgreSQL Integration

* Database creation and management using PostgreSQL.
* SQLAlchemy-based database connectivity.
* Automatic table generation from uploaded CSV files.

### 4. AI-Powered Natural Language Querying

* Integration with Google Gemini.
* Convert natural language questions into PostgreSQL queries.
* Execute generated SQL queries automatically.
* Return analytics results in JSON format.

### 5. Schema-Aware Query Generation

* Database schema is dynamically extracted.
* Gemini receives table and column metadata before SQL generation.
* Reduces hallucinations and improves query accuracy.

---

## Tech Stack

### Backend

* FastAPI
* Uvicorn

### Database

* PostgreSQL
* SQLAlchemy
* psycopg2

### Data Processing

* Pandas

### AI Layer

* Google Gemini API

### Development Tools

* Python
* VS Code
* pgAdmin

---

## Project Structure

```text
Project_Hydra/
│
├── app.py
├── database.py
├── csv_service.py
├── schema_service.py
├── ai_sql_generator.py
├── query_service.py
│
├── uploads/
│
├── requirements.txt
└── README.md
```

---

## Database Schema

### customers

| Column       |
| ------------ |
| CustomerID   |
| CustomerName |
| Email        |
| Phone        |
| State        |
| City         |
| JoinDate     |

### orders

| Column     |
| ---------- |
| OrderID    |
| CustomerID |
| ProductID  |
| Quantity   |
| OrderDate  |
| Status     |

### products

| Column      |
| ----------- |
| ProductID   |
| ProductName |
| Category    |
| Price       |

### sales_data

| Column       |
| ------------ |
| OrderID      |
| OrderDate    |
| CustomerID   |
| CustomerName |
| State        |
| City         |
| Product      |
| Category     |
| Quantity     |
| UnitPrice    |
| Revenue      |

---

## API Endpoints

### Upload Dataset

```http
POST /upload
```

Uploads a CSV file and stores it in PostgreSQL.

---

### List Available Datasets

```http
GET /datasets
```

Returns all available tables in the database.

---

### Dataset Preview

```http
GET /dataset/{table_name}
```

Returns the first few records from the selected dataset.

---

### Dataset Summary

```http
GET /dataset/{table_name}/summary
```

Returns:

* Number of rows
* Number of columns
* Missing values
* Column names

---

### Database Schema

```http
GET /schema
```

Returns metadata about tables and columns.

---

### Natural Language Query

```http
POST /query
```

Converts natural language into SQL using Gemini and executes the query.

---

## Example Questions

### Question 1

```text
show total revenue by state
```

Expected SQL:

```sql
SELECT "State",
       SUM("Revenue") AS total_revenue
FROM sales_data
GROUP BY "State"
ORDER BY total_revenue DESC;
```

Purpose:

* Revenue analytics
* Regional sales performance
* Business intelligence reporting

---

### Question 2

```text
show me customers from Gujarat state who ordered in 4th January, 2025
```

Expected SQL:

```sql
SELECT DISTINCT
       "CustomerName",
       "CustomerID",
       "City"
FROM sales_data
WHERE "State" = 'Gujarat'
  AND "OrderDate" = '2025-01-04';
```

Purpose:

* Customer segmentation
* Order tracking
* Regional customer analysis

---

## System Workflow

```text
User Question
      ↓
Gemini API
      ↓
SQL Generation
      ↓
PostgreSQL
      ↓
Query Execution
      ↓
Analytics Results
```

---

## Example Workflow

```text
Upload sales_data.csv
          ↓
Store in PostgreSQL
          ↓
User asks:
"show total revenue by state"
          ↓
Gemini generates SQL
          ↓
PostgreSQL executes query
          ↓
Results returned to user
```

---

## Future Enhancements

### Data Engineering

* Apache Kafka for real-time streaming ingestion
* Apache Airflow for workflow orchestration
* Data quality validation checks
* Automated ETL pipelines

### AI Features

* Query validation and correction
* Multi-step reasoning agents
* Schema-aware prompt engineering
* Query explanation generation

### Analytics

* Automatic chart generation
* Dashboard creation
* KPI monitoring
* Trend analysis

### Deployment

* Docker containerization
* Docker Compose
* CI/CD pipelines
* Kubernetes deployment

---

## Author

Jay Dave

M.Tech Computer Science & Engineering
Nirma University

Areas of Interest:

* Data Engineering
* Machine Learning
* MLOps
* GenAI
* Distributed Systems
