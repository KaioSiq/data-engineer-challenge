from application.controller import Controller
from infrastructure.messaging.kafka_consumer import KafkaConsumer
from infrastructure.file_handling.file_handling import FileHandler
import os

TOPIC_NAME = os.getenv("TOPIC_NAME", "poke-topic")
OUTPUT_FILE_NAME = os.getenv("OUTPUT_FILE_NAME", "type-count.json")


def main():
    # Instantiate the PokemonService
    pokemon_service = Controller(
        kafka_consumer=KafkaConsumer(TOPIC_NAME),
        file_handler=FileHandler(OUTPUT_FILE_NAME),
    )

    pokemon_service.consume_pokemon_from_topic()


if __name__ == "__main__":
    main()
