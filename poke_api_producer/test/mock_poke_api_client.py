import pathlib
import json
from ..entities.pokemon import Pokemon

class MockPokeApiClient:
    def get_pokemon_by_id(self, id: int):
        response = json.loads(pathlib.Path("poke_api_producer/test/api_return_value.json").read_text())
        return Pokemon.model_validate(response) 