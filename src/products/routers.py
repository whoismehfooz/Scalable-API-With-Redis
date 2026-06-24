from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.products.schemas import  ProductSchema, ProductResponseSchema
from src.products.controllers import register_new_product , get_product_by_id , get_all_products




product_router = APIRouter(prefix='/products', tags=['Products'])


@product_router.post('/', response_model=ProductResponseSchema, status_code=status.HTTP_201_CREATED)
async def register_product_endpoint(product: ProductSchema, db: Session = Depends(get_db)):
    return register_new_product(db, product)


@product_router.get('/{product_id}', response_model=ProductResponseSchema, status_code=status.HTTP_200_OK)
async def get_product_by_id_endpoint(product_id: int, db: Session = Depends(get_db)):
    return get_product_by_id(db, product_id)


@product_router.get('/', response_model=list[ProductResponseSchema], status_code=status.HTTP_200_OK)
async def get_all_products_endpoint(db: Session = Depends(get_db)):
    return get_all_products(db)