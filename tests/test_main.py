import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from main import app  # Absolute import
from models.product import Base  # Absolute import
from dependencies import get_db  # Absolute import

# Test database setup
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override dependency for testing
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Create tables
Base.metadata.create_all(bind=engine)

client = TestClient(app)

# Fixture to clean up database between tests
@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# Test functions
def test_create_product():
    response = client.post("/products/", json={"name": "Doll", "category": "Toy", "price": 10.99})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Doll"
    assert data["category"] == "Toy"
    assert data["price"] == 10.99

def test_get_products():
    client.post("/products/", json={"name": "Car", "category": "Toy", "price": 15.99})
    response = client.get("/products/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_filter_products_by_category():
    client.post("/products/", json={"name": "Puzzle", "category": "Game", "price": 20.0})
    response = client.get("/products/?category=Game")
    assert response.status_code == 200
    data = response.json()
    assert all(product["category"] == "Game" for product in data)

def test_get_product_not_found():
    response = client.get("/products/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"

def test_update_product():
    response = client.post("/products/", json={"name": "Ball", "category": "Toy", "price": 5.99})
    product_id = response.json()["id"]
    response = client.put(f"/products/{product_id}", json={"price": 7.99})
    assert response.status_code == 200
    assert response.json()["price"] == 7.99

def test_delete_product():
    response = client.post("/products/", json={"name": "Kite", "category": "Toy", "price": 12.99})
    product_id = response.json()["id"]
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Product deleted"