from confluent_kafka import Consumer, KafkaException
import os
import json

class KafkaConsumerClient:
    def __init__(self, group_id: str, topics: list[str]):
        self.consumer = Consumer({
            "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
            "group.id": group_id,
            "auto.offset.reset": "earliest",
            "enable.auto.commit": False
        })
        self.consumer.subscribe(topics)

    def poll(self, timeout: float = 1.0):
        msg = self.consumer.poll(timeout)
        if msg is None:
            return None
        if msg.error():
            raise KafkaException(msg.error())
        return {
            "topic": msg.topic(),
            "partition": msg.partition(),
            "offset": msg.offset(),
            "key": msg.key().decode("utf-8") if msg.key() else None,
            "value": json.loads(msg.value().decode("utf-8"))
        }

    def commit(self):
        self.consumer.commit()

    def close(self):
        self.consumer.close()