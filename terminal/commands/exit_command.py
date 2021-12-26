from models.command import Command
from program_context import ProgramContext


class ExitCommand(Command):
    def __init__(self):
        super().__init__("exit", "Exit the program.", aliases=["q"])

    def execute(self):
        ProgramContext.save()
        exit(0)
