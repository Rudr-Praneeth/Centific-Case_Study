from fastapi import APIRouter
from services.inventory_replenishment_service.api.routes.stock import router as stock_router

api_router = APIRouter()
api_router.include_router(stock_router)