from kafka import KafkaProducer

import json
import random
import time
from datetime import datetime

producer = KafkaProducer(
bootstrap_servers='localhost:9092',
value_serializer=lambda v:
json.dumps(v).encode('utf-8')
)

CUSTOMERS = [
"C001",
"C002",
"C003",
"C004",
"C005",
"C006",
"C007",
"C008",
"C009",
"C010"
]

PRODUCTS = [
"P001",
"P002",
"P003",
"P004",
"P005",
"P006",
"P007"
]

STATUSES = [
"Delivered"
]

order_id = 1000

while True:

    order = {
        "orderid": order_id,
        "customerid": random.choice(CUSTOMERS),
        "productid": random.choice(PRODUCTS),
        "quantity": random.randint(1, 5),
        "orderdate": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": random.choice(STATUSES)
    }

    producer.send(
        "orders_topic",
        order
    )

    producer.flush()

    print(
        f"Order Sent -> {order}"
    )

    order_id += 1

    time.sleep(5)
