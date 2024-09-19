import json
import os


class FileHandler:
    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def update_file(self, data):
        try:
            with open(self.file_path, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
           raise Exception(f"Error writing to file {self.file_path}: {e}")

    def read_file(self):
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, "r") as file:
                    return json.load(file)
            return {}
        except (IOError, OSError) as e:
            print(f"Error reading from file {self.file_path}: {e}")
            return {}
