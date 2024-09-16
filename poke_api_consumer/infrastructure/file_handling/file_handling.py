import json
import os


class FileHandler:
    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def update_file(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def read_file(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return json.load(file)
        return {}
