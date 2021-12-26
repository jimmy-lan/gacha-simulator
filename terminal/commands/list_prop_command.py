from models.command import Command
from program_context import ProgramContext


class ListPropCommand(Command):
    def __init__(self):
        super().__init__("prop", "List user properties.", aliases=["p"])

    def execute(self):
        wish_wit = ProgramContext.user_stats.num_wish_wits
        prop_map = ProgramContext.user_stats.properties

        print("--- [Property Summary] ---")
        print(f"wish wits * {wish_wit}")
        for name, quantity in prop_map.items():
            print(f"{name} * {quantity}")
