from kafka import KafkaConsumer

import json

from kafka_db_service import insert_order

consumer = KafkaConsumer(
"orders_topic",
bootstrap_servers='localhost:9092',
value_deserializer=lambda x:
json.loads(x.decode('utf-8'))
)

for message in consumer:

    print(message.value)

    insert_order(
        message.value
    )
