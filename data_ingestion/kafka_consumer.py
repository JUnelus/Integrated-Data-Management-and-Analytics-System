from kafka import KafkaConsumer
import json

# Initialize Kafka consumer
consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='transaction-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def consume_transactions():
    for message in consumer:
        transaction = message.value
        # Process transaction or push to transformation layer
        print(f"Consumed: {transaction}")

if __name__ == "__main__":
    consume_transactions()
