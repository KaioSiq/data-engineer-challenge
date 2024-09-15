import random
import time

from src.application.controller import PokemonController
from src.infrastructure.messaging.kafka_producer import KafkaProducerImpl
from src.infrastructure.poke_api.poke_api_client import PokeApiClientImpl


def main():
    controller = PokemonController(
        poke_api_client=PokeApiClientImpl(),
        kafka_producer=KafkaProducerImpl()
    )
    controller.run_pokemon_fetcher()                    

if __name__ == "__main__":
    main()
