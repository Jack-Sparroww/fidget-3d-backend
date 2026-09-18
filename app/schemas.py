from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class ProductVariationBase(BaseModel):
    color_name: str
    color_hex: str
    material: str
    stock_kg: float


class ProductVariationCreate(ProductVariationBase):
    pass


class ProductVariation(ProductVariationBase):
    id: int
    product_id: int

    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    base_price: float
    model_3d_url: str
    weight_g: float


class ProductCreate(ProductBase):
    variations: List[ProductVariationCreate] = []


class Product(ProductBase):
    id: int
    created_at: datetime
    variations: List[ProductVariation] = []

    class Config:
        from_attributes = True


class OrderItemCreate(BaseModel):
    product_id: int
    color_selected: str
    material_selected: str
    quantity: int


class OrderCreate(BaseModel):
    items: List[OrderItemCreate]
    shipping_address: str


class OrderStatusUpdate(BaseModel):
    status: str

    # Adicionar no final de app/schemas.py


class OrderCreate(BaseModel):
    user_id: int
    total_price: float
    shipping_cost: float


class Order(OrderCreate):
    id: int
    print_status: str

    class Config:
        from_attributes = True
