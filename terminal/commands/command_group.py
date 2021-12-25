from commands.command import Command


class CommandGroup(Command):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)
