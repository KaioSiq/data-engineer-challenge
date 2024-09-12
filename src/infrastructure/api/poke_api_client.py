import requests

from src.domain.pokemon.entities.pokemon import Pokemon


class PokeApiClientImpl:

    def __init__(self):
         self.poke_api_url = "https://pokeapi.co/api/v2/pokemon/"
    
    def get_pokemon_by_id(self, id_):
            try:
                response = requests.get(self.poke_api_url + id_)
                return Pokemon.model_validate(response.json())
            except Exception as e:
                print(f"Erro ao buscar Pokémon: {e}")
                raise
