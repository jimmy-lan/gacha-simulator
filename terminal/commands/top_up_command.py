from models.command import Command


class TopUpCommand(Command):
    top_up_item: str
    amount: float

    def __init__(self):
        super().__init__("topup", "Top up items. Syntax: topup <points|wit> <amount>.")

    def _report_invalid_syntax(self):
        self.print_help()
        raise Exception(f"Invalid syntax passed into command {self.name}.")

    def parse_arguments(self):
        if len(self.args) < 2:
            self._report_invalid_syntax()
        self.top_up_item = self.args[0]
        if self.top_up_item.lower() not in {"points", "wit"}:
            self._report_invalid_syntax()
        if not self.args[1].isdigit():
            self._report_invalid_syntax()
        self.amount = float(self.args[1])
        if self.amount <= 0 or self.amount > 100000:
            raise Exception("Invalid top up amount, out of acceptable range.")

    def execute(self):
        pass
