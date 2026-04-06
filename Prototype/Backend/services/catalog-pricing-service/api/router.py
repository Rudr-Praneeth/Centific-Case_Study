from fastapi import APIRouter
from services.catalog_pricing_service.api.routes.product import router as product_router

api_router = APIRouter()
api_router.include_router(product_router)