from fastapi import APIRouter
from services.identity_policy_service.api.routes.user_profile import router as user_profile_router

api_router = APIRouter()
api_router.include_router(user_profile_router)