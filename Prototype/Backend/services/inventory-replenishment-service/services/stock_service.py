from sqlalchemy.orm import Session
from services.inventory_replenishment_service.repositories.stock_repository import StockRepository
from services.inventory_replenishment_service.models.stock import Stock

class StockService:
    def __init__(self, db: Session):
        self.repo = StockRepository(db)
        self.db = db

    def create_stock(self, data: dict):
        entity = Stock(**data)
        result = self.repo.create(entity)
        self.db.commit()
        return result

    def get_stock(self, stock_id: str):
        return self.repo.get_by_id(stock_id)

    def list_by_product(self, product_id: str):
        return self.repo.list_by_product(product_id)

    def list_by_location(self, location_id: str):
        return self.repo.list_by_location(location_id)

    def update_stock(self, stock_id: str, data: dict):
        self.repo.update(stock_id, data)
        self.db.commit()

    def adjust_stock(self, stock_id: str, delta: int):
        self.repo.adjust_quantity(stock_id, delta)
        self.db.commit()