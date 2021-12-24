from constants.banner_rewards import BANNER_REWARDS
from constants.banner_rules import RARITY_WEIGHTS, PITY_MAX_DRAW, PITY_THRESHOLD
from controllers.banner import Banner
from controllers.persistence import Persistence
from models.banner_reward import BannerReward
from models.storage_key import StorageKey


def save_banner(banner: Banner) -> None:
    pass


def read_banner(banner: Banner) -> None:
    """
    Read information from disk and set banner in-place.
    """
    pity_count = Persistence(StorageKey.banner.value).read_json()
    banner.pity_count = pity_count
    banner.audit_pity_count()


def create_banner() -> Banner:
    """
    Initialize banner with constants and the current user statistics.
    """
    banner = Banner(RARITY_WEIGHTS)
    banner.pity_max_draw = PITY_MAX_DRAW
    banner.pity_threshold = PITY_THRESHOLD
    for rarity in BANNER_REWARDS:
        for item_name, quantity, weight in BANNER_REWARDS[rarity]:
            reward = BannerReward(item_name, quantity=quantity, weight=weight, rarity=rarity)
            banner.add_reward(reward)

    return banner
