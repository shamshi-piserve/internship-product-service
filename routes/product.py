from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.product import Product, ProductCreate, ProductUpdate  # Absolute import
from services.product import create_product, get_products, get_product, update_product, delete_product  # Absolute import
from dependencies import get_db  # Absolute import

router = APIRouter()

@router.post("/products/", response_model=Product)
def create_product_endpoint(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.get("/products/", response_model=List[Product])
def read_products(name: str | None = None, category: str | None = None, db: Session = Depends(get_db)):
    products = get_products(db, name=name, category=category)
    return products

@router.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/products/{product_id}", response_model=Product)
def update_product_endpoint(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    updated_product = update_product(db, product_id, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/products/{product_id}")
def delete_product_endpoint(product_id: int, db: Session = Depends(get_db)):
    if not delete_product(db, product_id):
        raise HTTPException(status_code=404, detail="Product not found")
    return {"detail": "Product deleted"}