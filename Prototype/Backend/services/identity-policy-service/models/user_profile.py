from sqlalchemy import Column, String, Boolean, DateTime, JSON
from sqlalchemy.sql import func
from shared.database.postgres import Base
import uuid

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False)
    role = Column(String, nullable=False)
    store_id = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    metadata = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())