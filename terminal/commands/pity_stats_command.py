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
              f"{get_rarity_display(RewardRarity.epic.value)} item.")
        print(f"- You have {super_rare_pity_count} wishes since your last " +
              f"{get_rarity_display(RewardRarity.super_rare.value)} item.")

    def print_probability(self):
        epic_weight = ProgramContext.banner.get_weight(RewardRarity.epic.value)
        super_rare_weight = ProgramContext.banner.get_weight(RewardRarity.super_rare.value)
        total_rarity_weight = ProgramContext.banner.total_rarity_weight
        next_epic_probability = epic_weight / total_rarity_weight * 100
        next_super_rare_probability = super_rare_weight / total_rarity_weight * 100
        print("--- [Probabilities] ---")
        print(f"- Probability of an {get_rarity_display(RewardRarity.epic.value)} item on " +
              f"your next wish is about {next_epic_probability}%.")
        print(f"- Probability of an {get_rarity_display(RewardRarity.super_rare.value)} item on " +
              f"your next wish is about {next_super_rare_probability}%.")

    def execute(self):
        self.print_pity_count()

