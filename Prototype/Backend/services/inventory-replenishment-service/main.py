from fastapi import FastAPI
from shared.logging.logger import configure_logging, get_logger
from services.inventory_replenishment_service.api.router import api_router

configure_logging()
logger = get_logger("inventory-replenishment-service")

app = FastAPI(title="Inventory Replenishment Service")

app.include_router(api_router)

@app.get("/health")
def health():
    return {"status": "ok"}