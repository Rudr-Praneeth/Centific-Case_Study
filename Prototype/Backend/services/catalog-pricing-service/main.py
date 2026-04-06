from fastapi import FastAPI
from shared.logging.logger import configure_logging, get_logger
from services.catalog_pricing_service.api.router import api_router

configure_logging()
logger = get_logger("catalog-pricing-service")

app = FastAPI(title="Catalog Pricing Service")

app.include_router(api_router)

@app.get("/health")
def health():
    return {"status": "ok"}