from confluent_kafka import Producer

# Configuração do produtor Kafka
conf = {
    'bootstrap.servers': 'localhost:9092'  # Endereço do servidor Kafka
}

# Criação do produtor Kafka
producer = Producer(conf)

# Função de callback para lidar com a confirmação de entrega
def delivery_report(err, msg):
    if err is not None:
        print(f'Message sent to topic {msg.topic()}')

class KafkaProducerImpl:

    def __init__(self):
        self.topic_name = "poke-topic"

    def send_message(self, message):

        # Envio da mensagem
        producer.produce(self.topic_name, message, callback=delivery_report)

        # Espera até que todas as mensagens sejam enviadas
        producer.flush()

