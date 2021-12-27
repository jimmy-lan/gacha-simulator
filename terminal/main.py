from commands.exit_command import ExitCommand
from commands.list_pity_command import ListPityCommand
from commands.list_prop_command import ListPropCommand
from commands.redeem_command import RedeemCommand
from commands.reset_command import ResetCommand
from commands.top_up_command import TopUpCommand
from commands.wish_command import WishCommand
from models.command_group import CommandGroup
from program_context import ProgramContext
from colorama import init, Fore

init(autoreset=True)


def print_welcome():
    print(Fore.BLUE + "*" * 60)
    print(Fore.BLUE + f"Welcome! You have {ProgramContext.user_stats.num_wish_wits} wish wits to spare.")
    print(Fore.BLUE + "*" * 60)


def get_root_cmd():
    command = CommandGroup("gacha-sim", "", subcommands=[
        ExitCommand(),
        ListPityCommand(),
        ListPropCommand(),
        RedeemCommand(),
        TopUpCommand(),
        WishCommand(),
        ResetCommand()
    ])
    return command


if __name__ == '__main__':
    ProgramContext.initialize()
    cmd = get_root_cmd()

    print_welcome()

    while True:
        rawInput = input(">>> ")
        if len(rawInput.strip()) == 0:
            continue
        try:
            cmd.run(rawInput)
        except Exception as e:
            print(f"[Error] {e}")
