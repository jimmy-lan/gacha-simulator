from typing import List, Dict

from commands.command import Command


class CommandGroup(Command):
    subcommands: List[Command]
    _subcommand_map: Dict[str, Command]

    def __init__(self, name: str, description: str, subcommands: List[Command]):
        super().__init__(name, description)
        self.subcommands = subcommands

    def _build_subcommand_map(self):
        self._subcommand_map = {}
        for subcommand in self.subcommands:
            self._subcommand_map[subcommand.name] = subcommand

    def _validate_subcommands(self):
        for subcommand in self.subcommands:
            if subcommand.name == self.name:
                raise Exception("Subcommand must not have the same name as the command group.")
