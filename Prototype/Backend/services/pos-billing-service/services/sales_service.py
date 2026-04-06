from sqlalchemy.orm import Session
from services.pos_billing_service.repositories.sale_repository import SaleRepository
from services.pos_billing_service.models.sale import Sale, SaleLine

class SaleService:
    def __init__(self, db: Session):
        self.repo = SaleRepository(db)
        self.db = db

    def create_sale(self, data: dict):
        sale_data = data.get("sale")
        lines_data = data.get("lines", [])

        sale = Sale(**sale_data)

        lines = []
        for line in lines_data:
            line["sale_id"] = sale.id
            lines.append(SaleLine(**line))

        result = self.repo.create_sale(sale, lines)
        self.db.commit()
        return result

    def get_sale(self, sale_id: str):
        return self.repo.get_sale(sale_id)

    def get_sale_details(self, sale_id: str):
        sale = self.repo.get_sale(sale_id)
        lines = self.repo.get_sale_lines(sale_id)
        return {
            "sale": sale,
            "lines": lines
        }