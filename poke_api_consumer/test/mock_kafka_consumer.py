from ..entities.pokemon import Pokemon

class KafkaConsumerMock:
    def __init__(self):
        self.topic_name = "poke-topic"

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