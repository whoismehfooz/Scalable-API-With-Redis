from fastapi import FastAPI 
from src.utils.db import Base, engine
from src.products.models import ProductModel
from src.products.routers import product_router
from src.middleware.rate_limit import RateLimitMiddleware




app = FastAPI(title='Scalable API with Redis', description='A scalable API built with FastAPI and Redis', version='1.0.0')

Base.metadata.create_all(bind=engine)
app.include_router(product_router)
app.add_middleware(RateLimitMiddleware)