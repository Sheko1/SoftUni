class Song:
    def __init__(self, name: str, length: float, single: bool):
        self.single = single
        self.length = length
        self.name = name

    def get_info(self):
        return f"{self.name} - {self.length}"
