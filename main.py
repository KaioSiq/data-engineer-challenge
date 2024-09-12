from src.domain.pokemon.services.pokemon_service import PokemonService


def main():
    # Instantiate the PokemonService
    pokemon_service = PokemonService()

    for i in range(130,140):
        pokemon_service.send_pokemon_to_topic_by_id(str(i))

if __name__ == "__main__":
    main()