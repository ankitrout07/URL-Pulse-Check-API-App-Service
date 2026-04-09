# How to Run: Pulse-Check API

This guide provides step-by-step instructions for running the Pulse-Check API application locally, via Docker, and deploying the infrastructure via Terraform.

## 1. Running Locally (Python VENV)

**Prerequisites:** Python 3.11+ and PostgreSQL (optional, you can use SQLite for tests).

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ankitrout07/URL-Pulse-Check-API-App-Service-.git
   cd URL-Pulse-Check-API-App-Service-
   ```

2. **Set up the virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   ```bash
   cp .env.example .env
   # Open .env and set your DATABASE_URL if using PostgreSQL.
   ```

4. **Run the FastAPI server:**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```
   *The API will be available at `http://localhost:8000` and the interactive Swagger docs at `http://localhost:8000/docs`.*

---

## 2. Running via Docker

If you prefer not to install Python locally, you can run the app using Docker.

1. **Build the image:**
   ```bash
   docker build -t pulse-check-api .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8000:8000 -e DATABASE_URL="postgresql://user:pass@host:5432/dbname" pulse-check-api
   ```

---

## 3. Running Automated Tests

The tests use an in-memory SQLite database, so you don't need a live database running to test the logic.

1. **Activate your environment:**
   ```bash
   source venv/bin/activate
   ```

2. **Run pytest:**
   ```bash
   pytest tests/ -v
   ```

---

## 4. Deploying the Infrastructure (Terraform)

You can provision all necessary Azure resources (App Service, Postgres Database, Resource Group) using the provided Terraform scripts.

**Prerequisites:** Azure CLI (`az login` must be run first) and Terraform CLI must be installed.

1. **Navigate to the `infra` directory:**
   ```bash
   cd infra
   ```

2. **Set your database password securely:**
   *(Never commit this password to your code!)*
   ```bash
   export TF_VAR_db_password="YourSecurePasswordHere"
   ```

3. **Initialize and apply Terraform:**
   ```bash
   terraform init
   terraform plan
   terraform apply
   ```
   *(Review the plan and type `yes` when prompted to create the resources).*

Once applied, Terraform will output the URL of your new Azure Web App and the hostname of your PostgreSQL database!
