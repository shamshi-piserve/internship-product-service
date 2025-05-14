from fastapi import FastAPI
from routes import product  # Absolute import
from database import engine  # Absolute import
from models import product as product_model  # Absolute import

app = FastAPI(title="Product Service", description="API for managing products", version="1.0")

# Create database tables
product_model.Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(product.router)
