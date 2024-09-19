class FileHandlerMock:
    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def update_file(self, data):
        self.output_content = data

    def read_file(self):
        return {"types": {"ghost": 13, "poison": 13}}


class BrokenFileHandlerMock:
    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def update_file(self, data):
        self.output_content = data

    def read_file(self):
        raise Exception("Could not read file")
