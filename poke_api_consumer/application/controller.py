class Controller:
    def __init__(self, kafka_consumer, file_handler):
        self.file_handler = file_handler
        self.kafka_consumer = kafka_consumer

    def process_message(self):
        pokemon = self.kafka_consumer.consume_message()  # check
        self.type_counter(pokemon)

    def consume_pokemon_from_topic(self):
        while True:
            try:
                self.process_message()
            except Exception as e:
                print(f"Error processing Pokémon: {e}")

    def type_counter(self, pokemon):
        data = self.file_handler.read_file()
        type_counts = data.get("types", {})

        # Check if 'types' attribute exists and is a list
        if not hasattr(pokemon, "types") or not isinstance(pokemon.types, list):
            print(f"Error: Invalid Pokémon object structure: {pokemon}", flush=True)
            return

        pokemon_types = [ptype.type.name for ptype in pokemon.types]  # [agua, fofo]

        for ptype in pokemon_types:
            if ptype in type_counts:
                type_counts[ptype] += 1
            else:
                type_counts[ptype] = 1

        updated_data = {"types": type_counts}

        self.file_handler.update_file(updated_data)

        print(f"Updated type counts: {type_counts}", flush=True)
