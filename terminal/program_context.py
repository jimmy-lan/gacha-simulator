from controllers.banner import Banner
from helpers import create_banner, read_user_stats, save_user_stats, save_banner, read_banner
from models.user_stats import UserStats


class ProgramContext:
    banner: Banner = None
    user_stats: UserStats = None

    @staticmethod
    def initialize():
        ProgramContext.banner = create_banner()
        read_banner(ProgramContext.banner)
        ProgramContext.user_stats = UserStats()
        read_user_stats(ProgramContext.user_stats)

    @staticmethod
    def save_user_stats():
        save_user_stats(ProgramContext.user_stats)

    @staticmethod
    def save_banner_pity():
        save_banner(ProgramContext.banner)

    @staticmethod
    def save():
        ProgramContext.save_user_stats()
        ProgramContext.save_banner_pity()
