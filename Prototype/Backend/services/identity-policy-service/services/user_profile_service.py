from sqlalchemy.orm import Session
from services.identity_policy_service.repositories.user_profile_repository import UserProfileRepository
from services.identity_policy_service.models.user_profile import UserProfile

class UserProfileService:
    def __init__(self, db: Session):
        self.repo = UserProfileRepository(db)
        self.db = db

    def create_user_profile(self, data: dict):
        entity = UserProfile(**data)
        result = self.repo.create(entity)
        self.db.commit()
        return result

    def get_user_profile(self, user_id: str):
        return self.repo.get_by_user_id(user_id)

    def update_user_profile(self, user_id: str, data: dict):
        self.repo.update(user_id, data)
        self.db.commit()

    def deactivate_user(self, user_id: str):
        self.repo.deactivate(user_id)
        self.db.commit()