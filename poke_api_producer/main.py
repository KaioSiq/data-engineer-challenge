import random
import time

from application.controller import PokemonController
from infrastructure.messaging.kafka_producer import KafkaProducerImpl
from infrastructure.poke_api.poke_api_client import PokeApiClientImpl


def main():
    controller = PokemonController(
        poke_api_client=PokeApiClientImpl(),
        kafka_producer=KafkaProducerImpl()
    )
    controller.run_pokemon_fetcher()                    

if __name__ == "__main__":
    main()
