import requests
from entities.pokemon import Pokemon


class PokeApiClient:
    def __init__(self):
         self.poke_api_url = "https://pokeapi.co/api/v2/pokemon/"
    
    def get_pokemon_by_id(self, id: int) -> Pokemon:
            try:
                response = requests.get(self.poke_api_url + str(id))
                print(response)
                return Pokemon.model_validate(response.json())
            except Exception as e:
                raise Exception(f"Failed to fetch pokemon id {id}: {e}")
