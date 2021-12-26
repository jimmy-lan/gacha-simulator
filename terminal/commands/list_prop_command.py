from models.command import Command
from program_context import ProgramContext


class ListPropCommand(Command):
    def __init__(self):
        super().__init__("prop", "List user properties.", aliases=["p"])

    def execute(self):
        prop_map = ProgramContext.user_stats.properties
