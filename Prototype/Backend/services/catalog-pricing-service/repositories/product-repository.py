from sqlalchemy.orm import Session
from sqlalchemy import select, update
from services.catalog_pricing_service.models.product import Product

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, entity: Product):
        self.db.add(entity)
        self.db.flush()
        return entity

    def get_by_id(self, product_id: str):
        stmt = select(Product).where(Product.id == product_id)
        return self.db.execute(stmt).scalar_one_or_none()

    def get_by_sku(self, sku: str):
        stmt = select(Product).where(Product.sku == sku)
        return self.db.execute(stmt).scalar_one_or_none()

    def list(self, limit: int = 50, offset: int = 0):
        stmt = select(Product).offset(offset).limit(limit)
        return self.db.execute(stmt).scalars().all()

    def update(self, product_id: str, data: dict):
        stmt = (
            update(Product)
            .where(Product.id == product_id)
            .values(**data)
            .execution_options(synchronize_session="fetch")
        )
        self.db.execute(stmt)

    def deactivate(self, product_id: str):
        stmt = (
            update(Product)
            .where(Product.id == product_id)
            .values(is_active=False)
        )
        self.db.execute(stmt)