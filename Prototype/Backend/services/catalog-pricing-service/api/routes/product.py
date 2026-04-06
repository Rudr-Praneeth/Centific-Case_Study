from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from shared.database.postgres import get_db
from shared.security.dependencies import get_current_user, require_roles
from services.catalog_pricing_service.services.product_service import ProductService

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/")
def create_product(
    payload: dict,
    db: Session = Depends(get_db),
    user=Depends(require_roles(["admin"]))
):
    service = ProductService(db)
    result = service.create_product(payload)
    return result

@router.get("/{product_id}")
def get_product(
    product_id: str,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    service = ProductService(db)
    return service.get_product(product_id)

@router.get("/")
def list_products(
    limit: int = Query(50),
    offset: int = Query(0),
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    service = ProductService(db)
    return service.list_products(limit, offset)

@router.put("/{product_id}")
def update_product(
    product_id: str,
    payload: dict,
    db: Session = Depends(get_db),
    user=Depends(require_roles(["admin"]))
):
    service = ProductService(db)
    service.update_product(product_id, payload)
    return {"status": "updated"}

@router.delete("/{product_id}")
def deactivate_product(
    product_id: str,
    db: Session = Depends(get_db),
    user=Depends(require_roles(["admin"]))
):
    service = ProductService(db)
    service.deactivate_product(product_id)
    return {"status": "deactivated"}