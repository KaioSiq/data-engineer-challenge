import json
from ..entities.pokemon import Pokemon


from pathlib import Path

# Get the current file directory
current_dir = Path(__file__).parent.resolve()


class MockPokeApiClient:
    def get_pokemon_by_id(self, id: int):
        response = json.loads(Path(current_dir / "api_return_value.json").read_text())
        return Pokemon.model_validate(response)
