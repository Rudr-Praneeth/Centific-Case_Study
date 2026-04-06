from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from shared.database.postgres import get_db
from shared.security.dependencies import get_current_user, require_roles
from services.inventory_replenishment_service.services.stock_service import StockService

router = APIRouter(prefix="/stocks", tags=["Stocks"])

@router.post("/")
def create_stock(
    payload: dict,
    db: Session = Depends(get_db),
    user=Depends(require_roles(["inventory_manager"]))
):
    service = StockService(db)
    result = service.create_stock(payload)
    return result

@router.get("/{stock_id}")
def get_stock(
    stock_id: str,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    service = StockService(db)
    return service.get_stock(stock_id)

@router.get("/product/{product_id}")
def list_by_product(
    product_id: str,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    service = StockService(db)
    return service.list_by_product(product_id)

@router.get("/location/{location_id}")
def list_by_location(
    location_id: str,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    service = StockService(db)
    return service.list_by_location(location_id)

@router.put("/{stock_id}")
def update_stock(
    stock_id: str,
    payload: dict,
    db: Session = Depends(get_db),
    user=Depends(require_roles(["inventory_manager"]))
):
    service = StockService(db)
    service.update_stock(stock_id, payload)
    return {"status": "updated"}

@router.post("/{stock_id}/adjust")
def adjust_stock(
    stock_id: str,
    delta: int,
    db: Session = Depends(get_db),
    user=Depends(require_roles(["inventory_manager"]))
):
    service = StockService(db)
    service.adjust_stock(stock_id, delta)
    return {"status": "adjusted"}