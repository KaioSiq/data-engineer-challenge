from ..entities.pokemon import Pokemon


class KafkaConsumerMock:
    def __init__(self, topic_name):
        self.topic_name = topic_name

    def consume_message(self):
        message_dict = {
            "id": 484,
            "name": "palkia",
            "types": [
                {"slot": 1, "type": {"name": "water"}},
                {"slot": 2, "type": {"name": "poison"}},
            ],
        }
        return Pokemon.model_validate(message_dict)
