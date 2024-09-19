from application.controller import Controller
from infrastructure.messaging.kafka_producer import KafkaProducer
from infrastructure.poke_api.poke_api_client import PokeApiClient

import os

TOPIC_NAME = os.getenv("TOPIC_NAME", "poke-topic")


def main():
    controller = Controller(
        poke_api_client=PokeApiClient(),
        kafka_producer=KafkaProducer(topic_name=TOPIC_NAME),
    )
    controller.run_pokemon_fetcher()


if __name__ == "__main__":
    main()
