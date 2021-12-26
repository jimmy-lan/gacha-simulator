from time import sleep

from colorama import Fore

from constants.banner_rules import WISH_WIT_PRICE, MIN_WISHES, MAX_WISHES
from program_context import ProgramContext
from models.command import Command
from models.item_name import ItemName


class WishCommand(Command):
    num_wish: int

    def __init__(self):
        super().__init__("wish", "Make wishes using wish wit.", aliases=["r"])
        self.num_wish = 0

    def _parse_num_wish(self):
        if len(self.args) < 1:
            return 1
        if not self.args[0].isdigit():
            raise Exception(f"Invalid number of wishes passed into command {self.name}.")
        num_wish = int(self.args[0])
        if num_wish < MIN_WISHES or num_wish > MAX_WISHES:
            raise Exception(f"Number of wishes must be an integer between {MIN_WISHES} and {MAX_WISHES} inclusive.")
        return num_wish

    def get_num_wish(self):
        if not self.num_wish:
            self.num_wish = self._parse_num_wish()
        return self.num_wish

    def consume_wish_wit(self) -> bool:
        num_wish = self.get_num_wish()
        num_user_wit = ProgramContext.user_stats.num_wish_wits
        if num_user_wit < num_wish:
            diff = num_wish - num_user_wit
            price = diff * WISH_WIT_PRICE
            if ProgramContext.user_stats.properties[ItemName.points.value] < price:
                return False
            is_accept = input("You don't have enough wish wit for this roll. Do you want " +
                              f"to use {Fore.GREEN}{price}{Fore.RESET} points to redeem the missing wish wits? " +
                              "(yn) ")
            if is_accept.lower() != "y":
                return False
            ProgramContext.user_stats.properties[ItemName.points.value] -= price
        ProgramContext.user_stats.num_wish_wits = max(num_user_wit - num_wish, 0)
        return True

    def wait_for_next_wish(self):
        if self.get_num_wish() > 1:
            sleep(0.5)

    def perform_wish(self):
        num_wish = self.get_num_wish()
        # A mapping between rewards names and total quantity obtained.
        rewards_map = {}

        print("--- [Obtained] ---")
        for _ in range(num_wish):
            reward = ProgramContext.banner.wish()
            if reward.name in rewards_map:
                rewards_map[reward.name] += reward.quantity
            else:
                rewards_map[reward.name] = reward.quantity
            ProgramContext.user_stats.record_wish(reward)
            ProgramContext.user_stats.properties[reward.name] += reward.quantity
            print(reward)
            self.wait_for_next_wish()

        if self.get_num_wish() == 1:
            return
        print("-" * 30)
        print(f"--- [Wish Summary] ---")
        for name, quantity in rewards_map.items():
            print(f"- {name} * {quantity}")

    def execute(self):
        if not self.consume_wish_wit():
            raise Exception("Insufficient wish wits.")
        self.perform_wish()
        ProgramContext.save()
