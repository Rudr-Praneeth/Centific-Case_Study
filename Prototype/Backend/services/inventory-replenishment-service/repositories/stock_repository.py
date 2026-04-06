from sqlalchemy.orm import Session
from sqlalchemy import select, update
from services.inventory_replenishment_service.models.stock import Stock

class StockRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, entity: Stock):
        self.db.add(entity)
        self.db.flush()
        return entity

    def get_by_id(self, stock_id: str):
        stmt = select(Stock).where(Stock.id == stock_id)
        return self.db.execute(stmt).scalar_one_or_none()

    def list_by_product(self, product_id: str):
        stmt = select(Stock).where(Stock.product_id == product_id)
        return self.db.execute(stmt).scalars().all()

    def list_by_location(self, location_id: str):
        stmt = select(Stock).where(Stock.location_id == location_id)
        return self.db.execute(stmt).scalars().all()

    def update(self, stock_id: str, data: dict):
        stmt = (
            update(Stock)
            .where(Stock.id == stock_id)
            .values(**data)
            .execution_options(synchronize_session="fetch")
        )
        self.db.execute(stmt)

    def adjust_quantity(self, stock_id: str, delta: int):
        stmt = (
            update(Stock)
            .where(Stock.id == stock_id)
            .values(quantity=Stock.quantity + delta)
        )
        self.db.execute(stmt)