from confluent_kafka import Producer
import json
import os

class KafkaProducerClient:
    def __init__(self):
        self.producer = Producer({
            "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
            "acks": "all",
            "retries": 5,
            "linger.ms": 5,
            "enable.idempotence": True
        })

    def _delivery_report(self, err, msg):
        if err is not None:
            raise Exception(f"Delivery failed: {err}")

    def publish(self, topic: str, key: str, value: dict):
        payload = json.dumps(value).encode("utf-8")
        self.producer.produce(
            topic=topic,
            key=key,
            value=payload,
            callback=self._delivery_report
        )
        self.producer.poll(0)

    def flush(self):
        self.producer.flush()