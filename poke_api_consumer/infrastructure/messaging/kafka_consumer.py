import json
from confluent_kafka import Consumer, KafkaException, KafkaError
from entities.pokemon import Pokemon

# Configuração do produtor Kafka
consumer_conf = {
    'bootstrap.servers': 'localhost:9092',  # Endereço do broker Kafka
    'group.id': 'pokemon-consumer-group',   # Grupo do consumidor
    'auto.offset.reset': 'earliest'         # Começar a consumir desde o início
}

# Criar o consumidor
consumer = Consumer(consumer_conf)

# Função de callback para lidar com a confirmação de entrega
def delivery_report(err, msg):
    if err is not None:
        print(f'Mensagem enviada para o tópico {msg.topic()}')

class KafkaConsumerImpl:

    def __init__(self):
        self.topic_name = "poke-topic"
        consumer.subscribe([self.topic_name])


    def consume_message(self, topic_name):

        try:
            print(f"Consumindo mensagens do tópico '{topic_name}'...")
            while True:
                # Consumir uma mensagem
                message = consumer.poll(timeout=10.0)  # Timeout de 1 segundo
                if message is not None:
                    # Extrair e decodificar o valor da mensagem
                    message_value = message.value()

                    if isinstance(message_value, bytes):
                        # Decodifica bytes para string
                        message_value = message_value.decode('utf-8')

                    # Converter a string JSON para dicionário
                    message_dict = json.loads(message_value)

                    # Validar e retornar o objeto Pokemon
                    return Pokemon.model_validate(message_dict)

                # if message is None:
                #     continue  # Se não há mensagem, continue tentando

                # if message.error():
                #     if message.error().code() == KafkaError._PARTITION_EOF:
                #         # Fim da partição, continue consumindo
                #         continue
                #     else:
                #         # Outro erro
                #         raise KafkaException(message.error())
                # else:
                #     # Imprimir a mensagem consumida
                #     print(f"Mensagem recebida: {message.value().decode('utf-8')}")
                    

        except KeyboardInterrupt:
            print("Consumo interrompido.")

        # finally:
        #     # Fechar o consumidor
        #     consumer.close()


