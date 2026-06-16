from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v:
        json.dumps(v).encode("utf-8")
)


def send_sale_event(data):

    producer.send(
        "sales_topic",
        data
    )

    producer.flush()
