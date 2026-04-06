from fastapi import FastAPI
from shared.logging.logger import configure_logging, get_logger
from services.pos_billing_service.api.router import api_router

configure_logging()
logger = get_logger("pos-billing-service")

app = FastAPI(title="POS Billing Service")

app.include_router(api_router)

@app.get("/health")
def health():
    return {"status": "ok"}