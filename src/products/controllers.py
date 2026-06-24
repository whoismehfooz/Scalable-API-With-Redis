import json
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.products.schemas import ProductSchema
from src.products.models import ProductModel
from src.cache.redis_client import redis_client



# Register new product and invalidate cache.
def register_new_product(db: Session, product: ProductSchema):

    new_product = ProductModel(
        name=product.name,
        price=product.price
    ) 
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    redis_client.delete('all_products')
    
    return new_product


# Get product by id without caching.
def get_product_by_id(db: Session, product_id:int):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if not product:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Product with id {product_id} not found')
    
    return product


# Get all products wtih caching.
def get_all_products(db: Session):

    cached_products = redis_client.get('all_products')

    if cached_products:

        print('Cache Hit')
        return json.loads(cached_products)
    
    print('Cache Miss')

    products = db.query(ProductModel).all()

    product_data = [{
        'id': product.id,
        'name': product.name,
        'price': product.price
    }  for product in products]

    products_json = json.dumps(product_data)

    redis_client.set(
        'all_products',
        products_json,
        ex=60   )
    
    return product_data