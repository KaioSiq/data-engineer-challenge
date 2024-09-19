from ..application.controller import Controller
from .mock_file_handling import FileHandlerMock, BrokenFileHandlerMock
from .mock_kafka_consumer import KafkaConsumerMock
import pytest


def test_controller():
    controller = Controller(
        kafka_consumer=KafkaConsumerMock("poke=topic"),
        file_handler=FileHandlerMock("test.json"),
    )

    controller.process_message()

    assert controller.file_handler.output_content == {
        "types": {"ghost": 13, "poison": 14, "water": 1}
    }


def test_controller_broken_file_handler():
    controller = Controller(
        kafka_consumer=KafkaConsumerMock("poke=topic"),
        file_handler=BrokenFileHandlerMock("test.json"),
    )

    with pytest.raises(Exception):
        controller.process_message()
