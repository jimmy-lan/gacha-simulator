from typing import List


class Command:
    rawArgs: List[str]

    def __init__(self):
        self.rawArgs = []

    def execute(self):
        pass

    def run(self, rawArgs: List[str]):
        self.rawArgs = rawArgs
        self.execute()
