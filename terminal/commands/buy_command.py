from colorama import Fore

from constants.banner_rules import WISH_WIT_PRICE
from models.command import Command
from models.item_name import ItemName
from program_context import ProgramContext


class BuyCommand(Command):
    def __init__(self):
        super().__init__(
            "buy",
            "Buy wish wits using points in your account." +
            " Syntax: buy [num_wish_wits].",
            aliases=["purchase"]
        )

    def _calc_max_num_purchase(self):
        points = ProgramContext.user_stats.properties[ItemName.points.value]
        return int(points // WISH_WIT_PRICE)

    def get_num_purchase(self):
        max_num_purchase = self._calc_max_num_purchase()
        if max_num_purchase <= 0:
            raise Exception("Insufficient points for this transaction.")
        if len(self.args) < 1:
            return max_num_purchase
        if not self.args[0].isdigit():
            self.print_help()
            raise Exception("Please enter a valid number of wish wits to purchase.")
        num_purchase = int(self.args[0])
        if num_purchase > max_num_purchase:
            raise Exception("Insufficient points for this transaction.")
        return num_purchase

    def execute(self):
        num_purchase = self.get_num_purchase()
        ProgramContext.user_stats.properties[ItemName.points.value] -= num_purchase * WISH_WIT_PRICE
        ProgramContext.user_stats.num_wish_wits += num_purchase
        print(f"{Fore.GREEN}Success! You purchased {num_purchase} wish wits. Good luck!")
        ProgramContext.save_user_stats()
