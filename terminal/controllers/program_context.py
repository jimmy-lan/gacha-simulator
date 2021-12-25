from controllers.banner import Banner
from helpers import create_banner, read_user_stats
from models.user_stats import UserStats


class ProgramContext:
    banner: Banner = None
    user_stats: UserStats = None

    @staticmethod
    def initialize():
        ProgramContext.banner = create_banner()
        ProgramContext.user_stats = UserStats()
        read_user_stats(ProgramContext.user_stats)
