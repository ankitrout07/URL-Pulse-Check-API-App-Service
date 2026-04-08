# Pulse-Check API

A lightweight DevOps-centric health monitoring service built with **FastAPI** and **PostgreSQL**. This application tracks service uptime and latency, storing results in an Azure Database for PostgreSQL Flexible Server.

---

## 🚀 Features
* **Real-time Logging:** Capture status codes and latency (ms) for external services.
* **History Tracking:** Query the last 10 health checks via a REST endpoint.
* **Cloud Ready:** Optimized for deployment on **Azure App Service** with environment-based configuration.

---

## 🛠️ Tech Stack
* **Framework:** FastAPI (Python 3.11+)
* **Database:** PostgreSQL (Azure Flexible Server)
* **ORM:** SQLAlchemy
* **Infrastructure:** Azure App Service (Linux)

---

## 📂 Project Structure
```text
pulse-check/
├── app.py              # Main application logic and API routes
├── database.py         # SQLAlchemy engine and session configuration
├── requirements.txt    # Python dependencies
└── README.md           # Documentation