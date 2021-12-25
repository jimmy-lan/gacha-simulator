from typing import List, Dict

from models.command import Command


class CommandGroup(Command):
    subcommands: List[Command]
    _subcommand_map: Dict[str, Command]

    def __init__(self, name: str, description: str, subcommands: List[Command] = []):
        super().__init__(name, description)
        self.set_subcommands(subcommands)

    def set_subcommands(self, subcommands: List[Command]):
        self.subcommands = subcommands
        self._build_subcommand_map()
        self._validate_subcommands()

    def _build_subcommand_map(self):
        self._subcommand_map = {}
        for subcommand in self.subcommands:
            self._subcommand_map[subcommand.name] = subcommand
            for alias in subcommand.aliases:
                self._subcommand_map[alias] = subcommand

    def _validate_subcommands(self):
        for subcommand in self.subcommands:
            if subcommand.name == self.name:
                raise Exception("Subcommand must not have the same name as the command group.")

    def print_help(self):
        super().print_help()
        print(f"Available commands: {[subcommand.name for subcommand in self.subcommands]}")

    def execute(self):
        if len(self.args) < 1:
            self.print_help()
            return
        subcommand_name = self.args[0]
        self._subcommand_map[subcommand_name].run(self.args[1:])
