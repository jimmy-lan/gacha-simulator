from models.command import Command
from program_context import ProgramContext


class PityStatsCommand(Command):
    def __init__(self):
        super().__init__("stats", "List number of wishes since last item with rarity.", aliases=["s"])

    def execute(self):
        pity_count = ProgramContext.banner.pity_count
        print("--- [Pity Info] ---")
        for rarity, count in pity_count.items():
            print(f"- You have {count} wishes since your last {rarity} item.")
