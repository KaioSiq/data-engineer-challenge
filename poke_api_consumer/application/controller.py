class Controller:
    def __init__(self, kafka_consumer, file_handler):
        self.file_handler = file_handler
        self.kafka_consumer = kafka_consumer

    def process_message(self):
        try:
            pokemon = self.kafka_consumer.consume_message()  # check
            self.type_counter(pokemon)
        except Exception as e:
            raise Exception(f"Error processing Pokémon: {e}")

    def consume_pokemon_from_topic(self):
        while True:
            self.process_message()


    def type_counter(self, pokemon):
        data = self.file_handler.read_file()
        type_counts = data.get("types", {})
        if not hasattr(pokemon, "types") or not isinstance(pokemon.types, list):
            print(f"Error: Invalid Pokémon object structure: {pokemon}", flush=True)
            return

        pokemon_types = [ptype.type.name for ptype in pokemon.types]

        for ptype in pokemon_types:
            if ptype in type_counts:
                type_counts[ptype] += 1
            else:
                type_counts[ptype] = 1

        updated_data = {"types": type_counts}

        self.file_handler.update_file(updated_data)

        print(f"Updated type counts: {type_counts}", flush=True)
