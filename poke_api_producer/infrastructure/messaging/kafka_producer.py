import os

from confluent_kafka import Producer

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")

# Configuração do produtor Kafka
conf = {
    "bootstrap.servers": KAFKA_BROKER  # Endereço do servidor Kafka
}

# Criação do produtor Kafka
producer = Producer(conf)


# Função de callback para lidar com a confirmação de entrega
def delivery_report(err, msg):
    if err is not None:
        print(f"Message sent to topic {msg.topic()}")


class KafkaProducer:
    def __init__(self, topic_name=str):
        self.topic_name = topic_name

    def send_message(self, message):
        # Envio da mensagem
        producer.produce(self.topic_name, message, callback=delivery_report)

        # Espera até que todas as mensagens sejam enviadas
        producer.flush()
