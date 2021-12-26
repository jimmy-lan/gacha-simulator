from typing import List, Union

SPACE = " "


class Command:
    args: List[str]
    name: str
    aliases: List[str]
    description: str

    def __init__(self, name: str, description: str, aliases: List[str] = []):
        self.name = name
        self.aliases = aliases
        self.description = description
        self.args = []

    def audit_args(self):
        self.args = [arg for arg in self.args if arg]

    def execute(self):
        pass

    def run(self, rawInput: Union[str, List[str]]):
        self.args = rawInput.strip().split(SPACE) \
            if type(rawInput) is str else rawInput
        self.audit_args()
        self.execute()

    def print_help(self):
        print(f"{self.name}: {self.description}")
