# Product Service

A FastAPI-based microservice for managing products, developed as part of the internship assignment. This service provides REST APIs for creating, reading, updating, and deleting products, with filtering capabilities, input validation, error handling, interactive documentation, and comprehensive unit tests.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies](#technologies)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

---

## Project Overview
The Product Service is a microservice that manages product data (e.g., name, category, price) stored in a PostgreSQL database. It exposes REST APIs for CRUD operations (Create, Read, Update, Delete) and supports filtering products by name or category. Built with **FastAPI**, it includes input validation via **Pydantic**, database integration with **SQLAlchemy**, and auto-generated OpenAPI documentation. Unit tests ensure reliability using **Pytest**.

This project fulfills the internship assignment requirements, providing a robust foundation for a product management system.

---

## Features
- **CRUD Operations**: Create, read, update, and delete products via REST APIs.
- **Filtering**: Search products by name or category (e.g., find all "Toy" products).
- **Input Validation**: Ensures data integrity using Pydantic models.
- **Error Handling**: Returns clear error messages (e.g., "Product not found" for invalid IDs).
- **OpenAPI Documentation**: Interactive API explorer at `http://localhost:8000/docs`.
- **Unit Tests**: Comprehensive test suite for all API endpoints.
- **Database Persistence**: Stores data in PostgreSQL for reliability.

---

## Technologies
- **Python 3.9+**: Core programming language.
- **FastAPI**: Framework for building high-performance REST APIs.
- **SQLAlchemy**: Object-Relational Mapping (ORM) for database interactions.
- **Pydantic**: Data validation and serialization.
- **PostgreSQL**: Relational database for storing product data.
- **Psycopg2**: PostgreSQL adapter for Python.
- **Pytest**: Framework for writing and running unit tests.
- **Uvicorn**: ASGI server for running the FastAPI application.

---

## Setup Instructions
Follow these steps to set up and run the project locally.

### Prerequisites
Ensure you have the following installed:
- [Python 3.9+](https://www.python.org/downloads/) (select "Add Python to PATH" during installation)
- [PostgreSQL](https://www.postgresql.org/download/) (with pgAdmin for database management)
- [Git](https://git-scm.com/downloads) (for version control)
- [Visual Studio Code](https://code.visualstudio.com/) (recommended code editor)

### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/shamshi-piserve/internship-product-service.git
   cd internship-product-service
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   ```
   Activate it:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic psycopg2-binary pytest pytest-asyncio
   ```

4. **Set Up PostgreSQL**:
   - Install and start PostgreSQL.
   - Open **pgAdmin 4** (installed with PostgreSQL).
   - Connect to the default server (username: `postgres`, password: set during installation).
   - Create a database named `products_db`:
     - Right-click **Databases** > **Create > Database**.
     - Enter `products_db` and click **Save**.
   - Note your PostgreSQL password.

5. **Configure Database URL**:
   - Open `main.py` in a code editor (e.g., VS Code).
   - Update the `DATABASE_URL` with your PostgreSQL credentials:
     ```python
     DATABASE_URL = "postgresql://postgres:your_password@localhost:5432/products_db"
     ```
     Replace `your_password` with your actual PostgreSQL password.

---

## Running the Application
1. **Start the FastAPI Server**:
   ```bash
   uvicorn main:app --reload
   ```
   - The `--reload` flag enables auto-reload for development (updates on code changes).

2. **Access the Application**:
   - Open a web browser and navigate to:
     - `http://localhost:8000`: Base URL of the service.
     - `http://localhost:8000/docs`: Interactive OpenAPI documentation for testing APIs.
   - Use the `/docs` page to try APIs (e.g., create a product or filter by category).

3. **Stop the Server**:
   - Press `Ctrl + C` in the terminal to stop the server.

---

## API Endpoints
The Product Service provides the following REST APIs for managing products:

| Method | Endpoint                   | Description                              | Request Body Example                              | Query Parameters                     |
|--------|----------------------------|------------------------------------------|--------------------------------------------------|--------------------------------------|
| POST   | `/products/`              | Create a new product                     | ```json<br>{"name": "Doll", "category": "Toy", "price": 10.99}<br>``` | None                                 |
| GET    | `/products/`              | List all products (with optional filters)| None                                             | `name` (e.g., `Doll`), `category` (e.g., `Toy`) |
| GET    | `/products/{product_id}`  | Get a product by ID                      | None                                             | None                                 |
| PUT    | `/products/{product_id}`  | Update a product’s details               | ```json<br>{"price": 12.99}<br>```               | None                                 |
| DELETE | `/products/{product_id}`  | Delete a product                         | None                                             | None                                 |

### Example API Requests
- **Create a Product**:
  ```bash
  curl -X POST "http://localhost:8000/products/" -H "Content-Type: application/json" -d '{"name": "Doll", "category": "Toy", "price": 10.99}'
  ```
  Response:
_CLOSE_XAI_BLOCK_
  ```json
  {"id": 1, "name": "Doll", "category": "Toy", "price": 10.99}
  ```

- **List Products with Filter**:
  ```bash
  curl "http://localhost:8000/products/?category=Toy"
  ```
  Response:
  ```json
  [{"id": 1, "name": "Doll", "category": "Toy", "price": 10.99}]
  ```

- **Get a Product by ID**:
  ```bash
  curl "http://localhost:8000/products/1"
  ```
  Response:
  ```json
  {"id": 1, "name": "Doll", "category": "Toy", "price": 10.99}
  ```

- **Update a Product**:
  ```bash
  curl -X PUT "http://localhost:8000/products/1" -H "Content-Type: application/json" -d '{"price": 12.99}'
  ```
  Response:
  ```json
  {"id": 1, "name": "Doll", "category": "Toy", "price": 12.99}
  ```

- **Delete a Product**:
  ```bash
  curl -X DELETE "http://localhost:8000/products/1"
  ```
  Response:
  ```json
  {"detail": "Product deleted"}
  ```

---

## Testing
The project includes unit tests to verify API functionality.

### Running Tests
1. Ensure the virtual environment is activated:
   ```bash
   venv\Scripts\activate
   ```
2. Run all tests:
   ```bash
   pytest
   ```
   - This executes tests in the `tests` folder.
   - Expect 6 tests to pass, covering CRUD operations, filtering, and error handling.

### Test Details
- **Location**: `tests/test_main.py`
- **Database**: Uses an in-memory SQLite database to avoid modifying the PostgreSQL database.
- **Coverage**:
  - Creating a product and verifying its attributes.
  - Listing all products.
  - Filtering products by category.
  - Handling invalid product IDs (404 errors).
  - Updating a product’s details.
  - Deleting a product.

---

## Project Structure
The project is organized as follows:

```plaintext
internship-product-service/
├── main.py               # FastAPI application with API routes and database logic
├── README.md             # Project documentation (this file)
├── tests/                # Unit tests
│   ├── __init__.py       # Makes the tests folder a Python module
│   └── test_main.py      # Tests for API endpoints
└── venv/                 # Virtual environment (not tracked in Git)
```

---



---

*Built by Vimal for the internship assignment at Piserve.*