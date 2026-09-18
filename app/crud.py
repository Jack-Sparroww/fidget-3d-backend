from sqlalchemy.orm import Session
from app import models, schemas

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        name=product.name,
        description=product.description,
        base_price=product.base_price,
        model_3d_url=product.model_3d_url,
        weight_g=product.weight_g
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    
    for var in product.variations:
        db_var = models.ProductVariation(**var.dict(), product_id=db_product.id)
        db.add(db_var)
    
    db.commit()
    db.refresh(db_product)
    return db_product