from colorama import Fore

from helpers import get_rarity_display, round_to_decimals
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
              f"{get_rarity_display(RewardRarity.epic.value)} item.")
        print(f"- You have {super_rare_pity_count} wishes since your last " +
              f"{get_rarity_display(RewardRarity.super_rare.value)} item.")

    def print_probability(self):
        epic_weight = ProgramContext.banner.get_weight(RewardRarity.epic.value)
        super_rare_weight = ProgramContext.banner.get_weight(RewardRarity.super_rare.value)
        total_rarity_weight = ProgramContext.banner.total_rarity_weight
        next_epic_probability = round_to_decimals(epic_weight / total_rarity_weight * 100, 2)
        next_super_rare_probability = round_to_decimals(super_rare_weight / total_rarity_weight * 100, 2)
        print("--- [Probabilities] ---")
        print(f"- Probability of an {get_rarity_display(RewardRarity.epic.value)} item on " +
              f"your next wish is approximately {next_epic_probability}%.")
        print(f"- Probability of a {get_rarity_display(RewardRarity.super_rare.value)} item on " +
              f"your next wish is approximately {next_super_rare_probability}%.")
        print("--- [Probability Notes] ---")
        print(f"The probabilities of an {get_rarity_display(RewardRarity.epic.value)} item and a "
              + f"{get_rarity_display(RewardRarity.super_rare.value)} item can add up to more than "
              + f"{Fore.BLUE}100.0%{Fore.RESET}.")
        print(f"In such case, you are {Fore.BLUE}guaranteed{Fore.RESET} to get an epic or super rare item on your "
              + f"next wish.")
        print(f"Moreover, parts of the increased probability {Fore.BLUE}will be carried over{Fore.RESET} to the wish "
              + f"after your next wish.")

    def execute(self):
        self.print_pity_count()
        self.print_probability()

