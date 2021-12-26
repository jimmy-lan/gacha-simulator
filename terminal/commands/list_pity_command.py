from models.command import Command


class ListPityCommand(Command):
    def __init__(self):
        super().__init__("pity", "List number of wishes since last item with rarity.", aliases=["b"])
