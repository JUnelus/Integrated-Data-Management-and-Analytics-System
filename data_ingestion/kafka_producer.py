from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Sample data sources
def generate_transaction():
    return {
        'transaction_id': f"txn_{random.randint(1000, 9999)}",
        'user_id': f"user_{random.randint(1, 100)}",
        'amount': round(random.uniform(10.0, 1000.0), 2),
        'timestamp': datetime.utcnow().isoformat()
    }

def produce_transactions(topic='transactions'):
    while True:
        transaction = generate_transaction()
        producer.send(topic, transaction)
        print(f"Produced: {transaction}")
        time.sleep(1)

if __name__ == "__main__":
    produce_transactions()
