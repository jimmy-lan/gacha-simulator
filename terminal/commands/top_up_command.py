from models.command import Command


class TopUpCommand(Command):
    def __init__(self):
        super().__init__("topup", "Top up items. Syntax: topup <points|wit> <amount>.")
