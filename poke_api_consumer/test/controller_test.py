from ..application.controller import Controller
from .mock_file_handling import FileHandlerMock
from .mock_kafka_consumer import KafkaConsumerMock


def test_controller():
    controller = Controller(
        kafka_consumer=KafkaConsumerMock("poke=topic"),
        file_handler=FileHandlerMock("test.json"),
    )

    controller.process_message()

    assert controller.file_handler.output_content == {
        "types": {"ghost": 13, "poison": 14, "water": 1}
    }
