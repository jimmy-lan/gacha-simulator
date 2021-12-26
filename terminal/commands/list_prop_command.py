from models.command import Command


class ListPropCommand(Command):
    def __init__(self):
        super().__init__("prop", "List user properties.", aliases=["p"])
