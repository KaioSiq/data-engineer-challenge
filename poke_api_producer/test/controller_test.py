import json

from ..application.controller import Controller
from .mock_kafka_producer import MockKafkaProducer
from .mock_poke_api_client import MockPokeApiClient


def test_controller():
    controller = Controller(
        kafka_producer=MockKafkaProducer(topic_name="poke-topic"),
        poke_api_client=MockPokeApiClient(),
    )

    controller.fetch_and_send_pokemon()

    assert controller.kafka_producer.messages == [
        json.dumps(
            {
                "id": 1,
                "name": "bulbasaur",
                "types": [
                    {"slot": 1, "type": {"name": "grass"}},
                    {"slot": 2, "type": {"name": "poison"}},
                ],
            }
        )
    ]
