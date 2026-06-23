from pydantic import BaseModel
from typing import List


class Product(BaseModel):
    name: str
    price: float

    class Config:
        from_attributes = True


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float

    class Config: 
        from_attributes = True