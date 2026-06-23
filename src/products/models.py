from sqlalchemy import Column, Integer, String, Float
from utils.db import Base


class ProductModel(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    price = Column(Float, nullable=False)