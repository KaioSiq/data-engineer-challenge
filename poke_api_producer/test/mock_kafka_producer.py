class MockKafkaProducer:
    messages = []

    def __init__(self, topic_name: str):
        self.topic_name = topic_name

    def send_message(self, message):
        self.messages.append(message)
        