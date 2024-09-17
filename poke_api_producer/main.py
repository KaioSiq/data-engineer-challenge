from application.controller import Controller
from infrastructure.messaging.kafka_producer import KafkaProducer
from infrastructure.poke_api.poke_api_client import PokeApiClient


def main():
    controller = Controller(
        poke_api_client=PokeApiClient(),
        kafka_producer=KafkaProducer(topic_name="poke-topic"),
    )
    controller.run_pokemon_fetcher()


if __name__ == "__main__":
    main()
