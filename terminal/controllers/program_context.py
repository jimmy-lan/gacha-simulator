from controllers.banner import Banner
from helpers import create_banner
from models.user_stats import UserStats


class ProgramContext:
    banner: Banner
    user_stats: UserStats

    @staticmethod
    def initialize():
        ProgramContext.banner = create_banner()
        ProgramContext.user_stats = UserStats()
