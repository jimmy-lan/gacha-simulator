from typing import List

from commands.command import Command


class CommandGroup(Command):
    subcommands: List[Command]

    def __init__(self, name: str, description: str, subcommands: List[Command]):
        super().__init__(name, description)
        self.subcommands = subcommands
