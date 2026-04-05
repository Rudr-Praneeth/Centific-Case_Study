from sqlalchemy.orm import Session
from sqlalchemy import select, update
from services.identity_policy_service.models.user_profile import UserProfile

class UserProfileRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, entity: UserProfile):
        self.db.add(entity)
        self.db.flush()
        return entity

    def get_by_user_id(self, user_id: str):
        stmt = select(UserProfile).where(UserProfile.user_id == user_id)
        return self.db.execute(stmt).scalar_one_or_none()

    def update(self, user_id: str, data: dict):
        stmt = (
            update(UserProfile)
            .where(UserProfile.user_id == user_id)
            .values(**data)
            .execution_options(synchronize_session="fetch")
        )
        self.db.execute(stmt)

    def deactivate(self, user_id: str):
        stmt = (
            update(UserProfile)
            .where(UserProfile.user_id == user_id)
            .values(is_active=False)
        )
        self.db.execute(stmt)