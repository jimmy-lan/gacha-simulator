from models.command import Command


class RedeemCommand(Command):
    def __init__(self):
        super().__init__("redeem", "Redeem your rewards and clear your current inventory.")
