import json
import random
import time

MINUTE = 60


class Controller:
    def __init__(self, poke_api_client, kafka_producer):
        self.poke_api_client = poke_api_client
        self.kafka_producer = kafka_producer

    def get_random_id(self) -> int:
        return random.randint(1, 1024)

    def fetch_and_send_pokemon(self):
        pokemon_id = self.get_random_id()
        pokemon = self.poke_api_client.get_pokemon_by_id(pokemon_id)
        self.kafka_producer.send_message(json.dumps(pokemon.model_dump()))
        
    def run_pokemon_fetcher(self):
        while True: 
            self.fetch_and_send_pokemon()
            time.sleep(MINUTE)
