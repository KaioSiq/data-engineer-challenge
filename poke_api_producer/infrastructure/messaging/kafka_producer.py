import os

from confluent_kafka import Producer

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")


conf = {"bootstrap.servers": KAFKA_BROKER}

producer = Producer(conf)


def message_report(err, msg):
    if err is not None:
        print(f"Message sent to topic {msg.topic()}")


class KafkaProducer:
    def __init__(self, topic_name: str):
        self.topic_name = topic_name

    def send_message(self, message):
        producer.produce(
            self.topic_name, message, callback=message_report
        )
        print(f"Publishing to: {self.topic_name}\nMessage sent: {message}", flush=True)
        producer.flush()
