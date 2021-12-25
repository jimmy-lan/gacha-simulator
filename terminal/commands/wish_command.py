from typing import List

from models.command import Command


class WishCommand(Command):
    def __int__(self):
        super().__init__("wish", "Make wishes using wish wit.")

    def execute(self):
        pass
