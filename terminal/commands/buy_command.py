from constants.banner_rules import WISH_WIT_PRICE
from models.command import Command
from models.item_name import ItemName
from program_context import ProgramContext


class BuyCommand(Command):
    def __init__(self):
        super().__init__(
            "buy",
            "Buy wish wits using points in your account." +
            " Syntax: buy <num_wish_wits>."
        )

    def _calc_max_num_purchase(self):
        points = ProgramContext.user_stats.properties[ItemName.points.value]
        return points // WISH_WIT_PRICE

    def num_purchase(self):
        if len(self.args) < 1:
            return self._calc_max_num_purchase()
        if not self.args[0].isdigit():
            self.print_help()
            raise Exception("Please enter a valid number of wish wits to purchase.")
        return int(self.args[0])

    def execute(self):
        pass
