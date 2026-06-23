from fastapi import FastAPI 
from utils.db import Base, engine







app = FastAPI(title='Scalable API with Redis', description='A scalable API built with FastAPI and Redis', version='1.0.0')

Base.metadata.create_all(bind=engine)