from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from shared.database.postgres import get_db
from shared.security.dependencies import get_current_user, require_roles
from services.identity_policy_service.services.user_profile_service import UserProfileService

router = APIRouter(prefix="/user-profiles", tags=["User Profiles"])

@router.post("/")
def create_user_profile(
    payload: dict,
    db: Session = Depends(get_db),
    user=Depends(require_roles(["admin"]))
):
    service = UserProfileService(db)
    result = service.create_user_profile(payload)
    return result

@router.get("/{user_id}")
def get_user_profile(
    user_id: str,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    service = UserProfileService(db)
    return service.get_user_profile(user_id)

@router.put("/{user_id}")
def update_user_profile(
    user_id: str,
    payload: dict,
    db: Session = Depends(get_db),
    user=Depends(require_roles(["admin"]))
):
    service = UserProfileService(db)
    service.update_user_profile(user_id, payload)
    return {"status": "updated"}

@router.delete("/{user_id}")
def deactivate_user(
    user_id: str,
    db: Session = Depends(get_db),
    user=Depends(require_roles(["admin"]))
):
    service = UserProfileService(db)
    service.deactivate_user(user_id)
    return {"status": "deactivated"}