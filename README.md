---

# 📦 Flask Stock Management API

A simple RESTful API built with **Flask** for managing product stock quantities. The application supports **adding**, **removing**, and **checking stock** for products using **PostgreSQL** and **Flask-SQLAlchemy**. It also features **interactive Swagger UI documentation** via **Flasgger**.

---

## 🚀 Features

* **Add Stock:** Create or update product stock quantities.
* **Remove Stock:** Safely reduce stock with validation.
* **Check Stock:** View the current stock level for any product.
* **Database:** PostgreSQL for persistent storage.
* **ORM:** SQLAlchemy for interacting with the database.
* **API Docs:** Swagger UI for live API testing.
* **Logging:** Basic logging for monitoring and debugging.
* **Environment Config:** Secure `.env` file usage.

---

## 🛠️ Tech Stack

| Tool             | Purpose                    |
| ---------------- | -------------------------- |
| Python 3.8+      | Programming Language       |
| Flask            | Web Framework              |
| Flask-SQLAlchemy | ORM for PostgreSQL         |
| Flasgger         | Swagger Documentation      |
| PostgreSQL       | Relational Database        |
| python-dotenv    | Load environment variables |

---

## 📁 Project Structure

```
Inventory_service/
│
├── app.py                  # Main Flask application with API endpoints
├── config.py               # Database configuration and environment variables
├── models.py               # SQLAlchemy model for ProductStock
├── test.py                 # Unit tests for endpoints and model
├── requirements.txt        # Python dependencies
├── .env.example            # Example environment variable file
└── README.md               # Project documentation
```

---

## ✅ Prerequisites

* Python 3.8 or higher
* PostgreSQL installed and running
* `pip` and `git` installed

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/shamshi-piserve/internship-inventory-service.git
cd internship-inventory-service

```

### 2. Create a Virtual Environment

```bash
python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL

```bash
psql -U postgres
CREATE DATABASE inventory_db;
\q
```

### 5. Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` and update it with your PostgreSQL credentials:

```env
DB_USER=postgres
DB_PASS=your_secure_password
DB_HOST=localhost
DB_NAME=inventory_db
DB_PORT=5432
```

### 6. Initialize the Database

#### Option A: Without Flask-Migrate

```bash
python app.py
```

#### Option B: Using Flask-Migrate

```bash
flask db init
flask db migrate
flask db upgrade
```

### 7. Run the Application

```bash
python app.py
```

> 🌐 API Base URL: `http://localhost:5000`
> 📘 Swagger UI: `http://localhost:5000/apidocs`

---

## 📡 API Endpoints

| Method | Endpoint                    | Description                  |
| ------ | --------------------------- | ---------------------------- |
| POST   | `/stock/add`                | Add stock for a product      |
| POST   | `/stock/remove`             | Remove stock from a product  |
| GET    | `/stock/check/<product_id>` | Check current stock quantity |

---

## 📬 Example API Requests

### ✅ Add Stock

```bash
curl -X POST http://localhost:5000/stock/add \
-H "Content-Type: application/json" \
-d '{"product_id": 101, "quantity": 5}'
```

**Response:**

```json
{ "message": "Stock created" }
```

---

### ❌ Remove Stock

```bash
curl -X POST http://localhost:5000/stock/remove \
-H "Content-Type: application/json" \
-d '{"product_id": 101, "quantity": 2}'
```

**Response:**

```json
{ "message": "Stock removed" }
```

---

### 📊 Check Stock

```bash
curl http://localhost:5000/stock/check/101
```

**Response:**

```json
{
  "product_id": 101,
  "quantity": 3
}
```

---


## 🧪 Testing

Unit tests are written in `test.py` using Python's built-in `unittest` framework. These tests cover:

* ✅ `ProductStock` model
* 📮 API endpoints: `/stock/add`, `/stock/remove`, `/stock/check/<product_id>`

---

### ⚡ Run Tests with SQLite (for local development)

Use SQLite for faster and easier testing without needing PostgreSQL:

```bash
set TEST_DB=sqlite
.\venv\Scripts\python -m unittest test.py -v
```

---

### 🐘 Run Tests with PostgreSQL (production-like environment)

1. **Ensure the test database exists:**

```sql
psql -U postgres
CREATE DATABASE test_inventory_db;
\q
```

2. **Set environment variables:**

```bash
set TEST_DB=postgresql
set TEST_SQLALCHEMY_DATABASE_URI=postgresql://postgres:your_secure_password@localhost:5432/test_inventory_db
```

3. **Run the tests:**

```bash
.\venv\Scripts\python -m unittest test.py -v
```

---

### 🧪 Running Tests in PyCharm

1. Open `test.py` in PyCharm.
2. Right-click anywhere in the file and select **"Run 'Unittests in test.py'"**.
3. In the Run Configuration, ensure the working directory is set to the root of the project directory, e.g., the folder that contains app.py.

---


## 🧾 Database Schema

**Table: `product_stock`**

| Column      | Type    | Constraints               |
| ----------- | ------- | ------------------------- |
| product\_id | Integer | Primary Key               |
| quantity    | Integer | Not Null, Default: 0, ≥ 0 |

---

## 🤝 Contributing

1. Fork the repository
2. Create your branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to GitHub: `git push origin feature/your-feature`
5. Open a Pull Request 🚀

---
