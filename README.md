# FastAPI Data Engineering Labs

A hands-on repository for exploring **FastAPI in Data Engineering workflows**, focusing on building scalable REST APIs for **data ingestion, processing, and data services**.

This project demonstrates how APIs can be used as **data interfaces** to interact with pipelines, analytics systems, and distributed data platforms.

---

# Project Goals

The goal of this repository is to learn and implement **production-style API services for data engineering use cases**, including:

* Building REST APIs using FastAPI
* Designing API-driven data ingestion services
* Creating microservices for data workflows
* Understanding API architecture used in modern data platforms
* Integrating APIs with data processing frameworks

---

# Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn
* REST API
* JSON Data Processing

Future integrations may include:

* Apache Spark
* Airflow
* Snowflake
* AWS S3 / Azure Data Lake
* Docker

---

# Repository Structure

```
fastapi-data-platform
│
├── app
│   ├── main.py                # FastAPI application entry point
│   │
│   ├── routers                # API route definitions
│   │   └── ingestion.py
│   │
│   ├── models                 # Data models (Pydantic schemas)
│   │   └── schemas.py
│   │
│   ├── services               # Business logic layer
│   │   └── ingestion_service.py
│   │
│   └── utils                  # Utility/helper functions
│
├── ingestion                  # API ingestion experiments
│   └── rest_api_ingestion.py
│
├── tests                      # Unit tests
│
├── requirements.txt
├── README.md
└── Dockerfile
```

---

# FastAPI Architecture for Data Projects

```
Client Request
      │
      ▼
FastAPI Router
      │
      ▼
Service Layer
      │
      ▼
Data Processing Logic
      │
      ▼
Storage / Data Platform
```

This architecture helps build **clean, modular, and scalable data services**.

---

# Example API Endpoints

Example endpoints that may be implemented in this repository:

```
GET /health
GET /datasets
POST /ingest-data
GET /ingestion-status
```

Example request:

```
POST /ingest-data
```

Request Body:

```
{
  "source": "external_api",
  "dataset": "orders",
  "start_date": "2026-01-01"
}
```

---

# Running the Project Locally

### 1 Install Dependencies

```
pip install -r requirements.txt
```

### 2 Start FastAPI Server

```
uvicorn app.main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically generates API documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

Alternative documentation:

```
http://127.0.0.1:8000/redoc
```

---

# Example Use Cases for Data Engineering

This repository will explore APIs for:

* Data ingestion services
* Metadata APIs for data platforms
* Triggering data pipelines
* Querying processed datasets
* API-based analytics services

---

# Future Improvements

Planned enhancements for this repository:

* Async API ingestion services
* Pagination and filtering
* API authentication (JWT/OAuth)
* Rate limiting and retry handling
* Integration with data lakes
* Containerized deployment with Docker
* Integration with orchestration tools

---

# Learning Focus

This project is part of a continuous learning journey to understand:

* REST API architecture
* Data service design
* API-based data pipelines
* Microservices for data platforms
* Scalable backend systems

---

# Author

Dnyaneshwar Shelke
Data Engineer | Python | Cloud | Data Platforms

---

# License

This project is open-source and available under the MIT License.
