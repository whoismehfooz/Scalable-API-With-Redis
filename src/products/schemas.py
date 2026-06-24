from pydantic import BaseModel
from typing import List


class ProductSchema(BaseModel):
    name: str
    price: float

    class Config:
        from_attributes = True


class ProductResponseSchema(BaseModel):
    id: int
    name: str
    price: float

    class Config: 
        from_attributes = True