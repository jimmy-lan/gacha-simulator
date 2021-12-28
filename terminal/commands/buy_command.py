from constants.banner_rules import WISH_WIT_PRICE
from models.command import Command
from models.item_name import ItemName
from program_context import ProgramContext


class BuyCommand(Command):
    def __init__(self):
        super().__init__("buy", "Buy wish wits using points in your account.")

    def _calc_max_num_purchase(self):
        points = ProgramContext.user_stats.properties[ItemName.points.value]
        return points // WISH_WIT_PRICE

    def num_purchase(self):
        pass

    def execute(self):
        pass