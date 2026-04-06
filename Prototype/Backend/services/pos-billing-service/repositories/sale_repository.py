from sqlalchemy.orm import Session
from sqlalchemy import select
from services.pos_billing_service.models.sale import Sale, SaleLine

class SaleRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_sale(self, sale: Sale, lines: list[SaleLine]):
        self.db.add(sale)
        for line in lines:
            self.db.add(line)
        self.db.flush()
        return sale

    def get_sale(self, sale_id: str):
        stmt = select(Sale).where(Sale.id == sale_id)
        return self.db.execute(stmt).scalar_one_or_none()

    def get_sale_lines(self, sale_id: str):
        stmt = select(SaleLine).where(SaleLine.sale_id == sale_id)
        return self.db.execute(stmt).scalars().all()