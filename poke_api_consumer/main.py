from application.controller import Controller
from infrastructure.messaging.kafka_consumer import KafkaConsumer
from infrastructure.file_handling.file_handling import FileHandler


def main():
    # Instantiate the PokemonService
    pokemon_service = Controller(
        kafka_consumer=KafkaConsumer("poke-topic"),
        file_handler=FileHandler("type-count.json"),
    )

    pokemon_service.consume_pokemon_from_topic()


if __name__ == "__main__":
    main()
