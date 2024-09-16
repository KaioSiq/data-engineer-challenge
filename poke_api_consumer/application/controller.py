import json
import os
from dataclasses import asdict
from infrastructure.messaging.kafka_consumer import KafkaConsumerImpl

class PokemonService:
    def __init__(self):
        # Instantiate the API client
        self.kafka_consumer = KafkaConsumerImpl()
        self.type_count_file = 'C:\\Users\\Kaio Siqueira\\Desktop\\types-count.json'  # Path to store type counts
    
    def consume_pokemon_from_topic(self, topic_name):
        while True:
            try:
                # Consume Pokémon message from Kafka topic
                pokemon = self.kafka_consumer.consume_message(topic_name)
                
                # Log or print the received Pokémon object
                print(pokemon)

                # Process the Pokémon and update the type counter
                self.type_counter(pokemon)
            
            except Exception as e:
                # Handle any errors that occur during message consumption or processing
                print(f"Error processing Pokémon: {e}")
    
    def type_counter(self, pokemon):
        # Step 1: Load existing type count data from JSON file if exists, otherwise initialize an empty structure
        if os.path.exists(self.type_count_file):
            with open(self.type_count_file, 'r') as file:
                data = json.load(file)
                type_counts = data.get("types", {})
        else:
            type_counts = {}

        # Step 2: Extract the types from the Pokémon object using dot notation (assuming it's an object with attributes)
        pokemon_types = [ptype.type.name for ptype in pokemon.types]

        # Step 3: Update the type counts based on the Pokémon's types
        for ptype in pokemon_types:
            if ptype in type_counts:
                type_counts[ptype] += 1
            else:
                type_counts[ptype] = 1

        # Step 4: Save the updated type count data back to the JSON file under the "types" key
        updated_data = {"types": type_counts}
        with open(self.type_count_file, 'w') as file:
            json.dump(updated_data, file, indent=4)

        # Optionally, log the updated type counts
        print(f"Updated type counts: {type_counts}")
