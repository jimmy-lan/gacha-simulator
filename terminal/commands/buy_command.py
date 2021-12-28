from models.command import Command


class BuyCommand(Command):
    def __init__(self):
        super().__init__("buy", "Buy wish wits using points in your account.")
