from sqlalchemy.orm import Session
from sqlalchemy import select, update
from datetime import datetime
from shared.outbox.model import OutboxEvent

class OutboxRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_event(self, event: OutboxEvent):
        self.db.add(event)
        self.db.flush()

    def get_pending_events(self, limit: int = 100):
        stmt = (
            select(OutboxEvent)
            .where(OutboxEvent.status == "PENDING")
            .order_by(OutboxEvent.created_at.asc())
            .limit(limit)
            .with_for_update(skip_locked=True)
        )
        return self.db.execute(stmt).scalars().all()

    def mark_processed(self, event_id: str):
        stmt = (
            update(OutboxEvent)
            .where(OutboxEvent.id == event_id)
            .values(
                status="PROCESSED",
                processed_at=datetime.utcnow()
            )
        )
        self.db.execute(stmt)

    def mark_failed(self, event_id: str):
        stmt = (
            update(OutboxEvent)
            .where(OutboxEvent.id == event_id)
            .values(
                status="FAILED",
                retries=OutboxEvent.retries + 1
            )
        )
        self.db.execute(stmt)