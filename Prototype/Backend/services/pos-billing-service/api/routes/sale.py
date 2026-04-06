from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from shared.database.postgres import get_db
from shared.security.dependencies import get_current_user, require_roles
from services.pos_billing_service.services.sale_service import SaleService

router = APIRouter(prefix="/sales", tags=["Sales"])

@router.post("/")
def create_sale(
    payload: dict,
    db: Session = Depends(get_db),
    user=Depends(require_roles(["cashier", "manager"]))
):
    service = SaleService(db)
    result = service.create_sale(payload)
    return result

@router.get("/{sale_id}")
def get_sale(
    sale_id: str,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    service = SaleService(db)
    return service.get_sale(sale_id)

@router.get("/{sale_id}/details")
def get_sale_details(
    sale_id: str,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    service = SaleService(db)
    return service.get_sale_details(sale_id)