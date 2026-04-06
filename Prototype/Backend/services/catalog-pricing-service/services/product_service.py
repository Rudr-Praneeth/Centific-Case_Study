from sqlalchemy.orm import Session
from services.catalog_pricing_service.repositories.product_repository import ProductRepository
from services.catalog_pricing_service.models.product import Product

class ProductService:
    def __init__(self, db: Session):
        self.repo = ProductRepository(db)
        self.db = db

    def create_product(self, data: dict):
        entity = Product(**data)
        result = self.repo.create(entity)
        self.db.commit()
        return result

    def get_product(self, product_id: str):
        return self.repo.get_by_id(product_id)

    def list_products(self, limit: int = 50, offset: int = 0):
        return self.repo.list(limit, offset)

    def update_product(self, product_id: str, data: dict):
        self.repo.update(product_id, data)
        self.db.commit()

    def deactivate_product(self, product_id: str):
        self.repo.deactivate(product_id)
        self.db.commit()