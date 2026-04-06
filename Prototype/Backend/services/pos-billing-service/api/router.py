from fastapi import APIRouter
from services.pos_billing_service.api.routes.sale import router as sale_router

api_router = APIRouter()
api_router.include_router(sale_router)