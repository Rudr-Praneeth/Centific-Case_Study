from sqlalchemy import Column, String, DateTime, Numeric, Integer, JSON
from sqlalchemy.sql import func
from shared.database.postgres import Base
import uuid

class Sale(Base):
    __tablename__ = "sales"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    store_id = Column(String, nullable=False)
    total_amount = Column(Numeric(10, 2), nullable=False)
    currency = Column(String, nullable=False, default="INR")
    status = Column(String, nullable=False)
    metadata = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class SaleLine(Base):
    __tablename__ = "sale_lines"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    sale_id = Column(String, nullable=False)
    product_id = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Numeric(10, 2), nullable=False)
    total_price = Column(Numeric(10, 2), nullable=False)