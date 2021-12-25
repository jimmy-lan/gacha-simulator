from typing import List

from colorama import Fore

from constants.banner_rules import WISH_WIT_PRICE
from controllers.program_context import ProgramContext
from models.command import Command
from models.item_name import ItemName


class WishCommand(Command):
    def __int__(self):
        super().__init__("wish", "Make wishes using wish wit.", aliases=["r"])

    def consume_wish_wit(self, num_wish: int) -> bool:
        num_user_wit = ProgramContext.user_stats.wish_wit
        if num_user_wit < num_wish:
            diff = num_wish - num_user_wit
            price = diff * WISH_WIT_PRICE
            if ProgramContext.user_stats.properties[ItemName.points.value] < price:
                return False
            is_accept = input("You don't have enough wish wit for this roll. Do you want " +
                              f"to use {Fore.GREEN}{price}{Fore.RESET} points to redeem the missing wish wits? " +
                              "(yn)")
            if is_accept.lower() != "y":
                return False
            ProgramContext.user_stats.properties[ItemName.points.value] -= price
        ProgramContext.user_stats.wish_wit = max(num_user_wit - num_wish, 0)
        return True

    def get_num_wish(self):
        if len(self.args) < 1:
            return 1
        if not self.args[0].isdigit():
            raise Exception(f"Invalid number of wishes passed into command {self.name}.")
        num_wish = int(self.args[0])
        if num_wish < 1 or num_wish > 10:
            raise Exception(f"Number of wishes must be an integer between 1 and 10 inclusive.")
        return num_wish

    def execute(self):
        pass
