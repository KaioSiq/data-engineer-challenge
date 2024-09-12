from src.domain.pokemon.services.pokemon_service import PokemonService


def main():
    # Instantiate the PokemonService
    pokemon_service = PokemonService()

    # Example pokemon_id
    pokemon_id = "7"

    for i in range(1,100):
        pokemon = pokemon_service.get_pokemon_by_id(str(i))

        # Print the result
        print(pokemon)

if __name__ == "__main__":
    main()