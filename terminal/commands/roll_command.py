from typing import List

from models.command import Command


class RollCommand(Command):
    def __int__(self, name: str, description: str, aliases: List[str] = []):
        super().__init__(name, description, aliases=aliases)
