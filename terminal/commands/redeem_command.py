from constants.item_ids import ITEM_IDS
from models.command import Command
from program_context import ProgramContext


class RedeemCommand(Command):
    def __init__(self):
        super().__init__("redeem", "Redeem your rewards and clear your current inventory.")

    def execute(self):
        prop_map = ProgramContext.user_stats.properties

        print("--- [Redeem Commands] ---")
        for item_name, quantity in prop_map.items():
            print(f"habits transaction create --property-id {ITEM_IDS[item_name]} -t \"[Redeem] Wish Rewards\" " +
                  f"-a {quantity}")

        ProgramContext.user_stats.properties = {}
        ProgramContext.user_stats.audit_properties()
        ProgramContext.save_user_stats()
