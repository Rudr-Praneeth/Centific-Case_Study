from fastapi import FastAPI
from shared.logging.logger import configure_logging, get_logger
from services.identity_policy_service.api.router import api_router

configure_logging()
logger = get_logger("identity-policy-service")

app = FastAPI(title="Identity Policy Service")

app.include_router(api_router)

@app.get("/health")
def health():
    return {"status": "ok"}