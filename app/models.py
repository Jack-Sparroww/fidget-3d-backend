from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.database import Base

class MaterialType(str, enum.Enum):
    PLA = "PLA"
    PETG = "PETG"

class OrderStatus(str, enum.Enum):
    PENDING_PAYMENT = "Aguardando Pagamento"
    PAID = "Pago"
    PRINTING = "Imprimindo"
    FINISHING = "Acabamento"
    SHIPPED = "Enviado"
    DELIVERED = "Entregue"
    CANCELLED = "Cancelado"

class UserRole(str, enum.Enum):
    CLIENT = "client"
    ADMIN = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default=UserRole.CLIENT)
    created_at = Column(DateTime, default=datetime.utcnow)

    orders = relationship("Order", back_populates="user")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    base_price = Column(Float, nullable=False)
    model_3d_url = Column(String, nullable=False)
    weight_g = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    variations = relationship("ProductVariation", back_populates="product")

class ProductVariation(Base):
    __tablename__ = "product_variations"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    color_name = Column(String, nullable=False)
    color_hex = Column(String, nullable=False)
    material = Column(String, default=MaterialType.PLA)
    stock_kg = Column(Float, default=1.0)

    product = relationship("Product", back_populates="variations")

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total_amount = Column(Float, nullable=False)
    status = Column(String, default=OrderStatus.PENDING_PAYMENT)
    shipping_address = Column(Text, nullable=False)
    tracking_code = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    color_selected = Column(String, nullable=False)
    material_selected = Column(String, nullable=False)
    quantity = Column(Integer, default=1)
    unit_price = Column(Float, nullable=False)

    order = relationship("Order", back_populates="items")