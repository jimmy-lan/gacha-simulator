from typing import List


class Command:
    rawArgs: List[str]
    name: str
    description: str

    def __init__(self, name: str, description: str):
        self.name = name
        self.rawArgs = []
        self.description = description

    def execute(self):
        pass

    def run(self, rawArgs: List[str]):
        self.rawArgs = rawArgs
        self.execute()

    def print_help(self):
        print(f"{self.name}: {self.description}")
