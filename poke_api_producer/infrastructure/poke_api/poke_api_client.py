import requests
from entities.pokemon import Pokemon


BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


class PokeApiClient:
    def __init__(self):
        self.poke_api_url = BASE_URL

    def get_pokemon_by_id(self, id: int) -> Pokemon:
        try:
            response = requests.get(self.poke_api_url + str(id))
            return Pokemon.model_validate(response.json())
        except Exception as e:
            raise Exception(f"Failed to fetch pokemon id {id}: {e}")
