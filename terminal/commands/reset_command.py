from colorama import Fore

from models.command import Command
from program_context import ProgramContext


class ResetCommand(Command):
    def __init__(self):
        super().__init__("reset", "Reset gacha game.")

    def execute(self):
        print(Fore.YELLOW + "[Note] This is a dangerous operation. Please confirm three (3) times below.")
        for _ in range(3):
            accepted_input = input(f"This will clear {Fore.RED}ALL GAME DATA{Fore.RED}. Continue? (yn) ")
            if accepted_input.lower() != "y":
                raise Exception("Reset failed: Cancelled by the user.")
                return
        ProgramContext.reset()
        print(Fore.YELLOW + "[Success] Program reset.")
