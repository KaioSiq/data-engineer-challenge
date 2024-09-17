import json
import os

from confluent_kafka import Consumer, KafkaError, KafkaException
from entities.pokemon import Pokemon

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")


consumer_conf = {
    "bootstrap.servers": KAFKA_BROKER,
    "group.id": "pokemon-consumer-group",
    "auto.offset.reset": "earliest",
}


consumer = Consumer(consumer_conf)


def delivery_report(err, msg):
    if err is not None:
        print(f"Mensagem enviada para o tópico {msg.topic()}")


class KafkaConsumer:
    def __init__(self, topic_name):
        self.topic_name = topic_name
        consumer.subscribe([self.topic_name])

    def consume_message(self):
        try:
            while True:
                message = consumer.poll(timeout=10.0)  # Timeout de 10 segundos
                if message is not None:
                    message_value = message.value()

                    if isinstance(message_value, bytes):
                        message_value = message_value.decode("utf-8")

                    message_dict = json.loads(message_value)

                    return Pokemon.model_validate(message_dict)

                if message is None:
                    continue

                if message.error():
                    if message.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    else:
                        raise KafkaException(message.error())
                else:
                    print(f"Mensagem recebida: {message.value().decode('utf-8')}")

        except KeyboardInterrupt:
            print("Consumo interrompido.")

        # finally:  ## handle
        #     consumer.close()
