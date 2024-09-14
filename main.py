import random
from src.domain.pokemon.services.pokemon_service import PokemonService

def main():
    # Instantiate the PokemonService
    pokemon_service = PokemonService()

    # Loop from 400 to 500
    for _ in range(1, 10):
        # Generate a random integer between 1 and 1024
        random_pokemon_id = random.randint(1, 1024)
        
        # Send the randomly generated Pokemon ID to the service
        pokemon_service.send_pokemon_to_topic_by_id(str(random_pokemon_id))

if __name__ == "__main__":
    main()
