import json


from src.infrastructure.api.poke_api_client import PokeApiClientImpl
from src.infrastructure.messaging.kafka_producer import KafkaProducerImpl

class PokemonService:
    def __init__(self):
        # Instantiate the API client
        self.poke_api_client = PokeApiClientImpl()
        self.kafka_producer = KafkaProducerImpl()

    def get_pokemon_by_id(self, id_):
        # Call the method on the instance of PokeApiClientImpl
        pokemon = self.poke_api_client.get_pokemon_by_id(id_)
        return pokemon
    
    def send_pokemon_to_topic_by_id(self, id_):
        pokemon = self.poke_api_client.get_pokemon_by_id(id_)
        self.kafka_producer.send_message(json.dumps(pokemon.model_dump()))
