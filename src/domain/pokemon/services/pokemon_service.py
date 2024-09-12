from src.infrastructure.api.poke_api_client import PokeApiClientImpl


class PokemonService:
    def __init__(self):
        # Instantiate the API client
        self.poke_api_client = PokeApiClientImpl()

    def get_pokemon_by_id(self, id_):
        # Call the method on the instance of PokeApiClientImpl
        pokemon = self.poke_api_client.get_pokemon_by_id(id_)
        return pokemon
