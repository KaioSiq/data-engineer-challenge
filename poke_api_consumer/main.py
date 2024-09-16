from application.controller import PokemonService


def main():
    # Instantiate the PokemonService
    pokemon_service = PokemonService()
    pokemon = pokemon_service.consume_pokemon_from_topic("poke-topic")
    pokemon_service.type_counter(pokemon)

    

if __name__ == "__main__":
    main()