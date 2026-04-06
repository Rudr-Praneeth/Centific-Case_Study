from sqlalchemy import Column, String, DateTime, Numeric, Boolean, JSON
from sqlalchemy.sql import func
from shared.database.postgres import Base
import uuid

class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    sku = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    category = Column(String, nullable=True)
    price = Column(Numeric(10, 2), nullable=False)
    currency = Column(String, nullable=False, default="INR")
    tax_rate = Column(Numeric(5, 2), nullable=False)
    is_active = Column(Boolean, default=True)
    metadata = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())