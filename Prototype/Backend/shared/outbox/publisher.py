from sqlalchemy.orm import Session
from shared.outbox.repository import OutboxRepository
from shared.kafka.producer import KafkaProducerClient

class OutboxPublisher:
    def __init__(self, db: Session):
        self.db = db
        self.repo = OutboxRepository(db)
        self.producer = KafkaProducerClient()

    def publish_events(self, topic_map: dict):
        events = self.repo.get_pending_events()

        for event in events:
            try:
                topic = topic_map.get(event.event_type)
                if not topic:
                    raise Exception("No topic mapping found")

                self.producer.publish(
                    topic=topic,
                    key=event.aggregate_id,
                    value={
                        "event_id": event.id,
                        "aggregate_type": event.aggregate_type,
                        "aggregate_id": event.aggregate_id,
                        "event_type": event.event_type,
                        "payload": event.payload,
                        "created_at": str(event.created_at)
                    }
                )

                self.repo.mark_processed(event.id)

            except Exception:
                self.repo.mark_failed(event.id)

        self.db.commit()
        self.producer.flush()