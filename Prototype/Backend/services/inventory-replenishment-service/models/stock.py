from sqlalchemy import Column, String, Integer, DateTime, Numeric
from sqlalchemy.sql import func
from shared.database.postgres import Base
import uuid

class Stock(Base):
    __tablename__ = "stocks"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    product_id = Column(String, nullable=False)
    location_id = Column(String, nullable=False)
    batch_number = Column(String, nullable=True)
    expiry_date = Column(DateTime(timezone=True), nullable=True)
    quantity = Column(Integer, nullable=False, default=0)
    reserved_quantity = Column(Integer, nullable=False, default=0)
    reorder_level = Column(Integer, nullable=True)
    unit_cost = Column(Numeric(10, 2), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())