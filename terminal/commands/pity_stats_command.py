from colorama import Fore

from constants.rarity_colors import RARITY_COLORS
from helpers import get_rarity_display
from models.command import Command
from models.reward_rarity import RewardRarity
from program_context import ProgramContext


class PityStatsCommand(Command):
    def __init__(self):
        super().__init__("stats", "List number of wishes since last item with rarity.", aliases=["s", "stat"])

    def print_pity_count(self):
        pity_count = ProgramContext.banner.pity_count
        epic_pity_count = pity_count[RewardRarity.epic.value]
        super_rare_pity_count = pity_count[RewardRarity.super_rare.value]
        print("--- [Pity Stats] ---")
        print(f"- You have {epic_pity_count} wishes since your last " +
              f"{get_rarity_display(RewardRarity.epic)} item.")
        print(f"- You have {super_rare_pity_count} wishes since your last " +
              f"{get_rarity_display(RewardRarity.super_rare)} item.")

    def execute(self):
        self.print_pity_count()

