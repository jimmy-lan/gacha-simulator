from constants.banner_rewards import BANNER_REWARDS
from constants.banner_rules import RARITY_WEIGHTS, PITY_MAX_DRAW, PITY_THRESHOLD
from controllers.banner import Banner
from controllers.persistence import Persistence
from models.banner_reward import BannerReward
from models.storage_key import StorageKey
from models.user_stats import UserStats


def save_banner(banner: Banner) -> None:
    """
    Save banner to disk.
    """
    Persistence(StorageKey.banner.value).save_json(banner.pity_count)


def read_banner(banner: Banner) -> None:
    """
    Read information from disk and set banner in-place.
    """
    try:
        pity_count = Persistence(StorageKey.banner.value).read_json()
    except Exception as e:
        return
    banner.pity_count = pity_count
    banner.audit_pity_count()


def save_user_stats(user_stats: UserStats) -> None:
    Persistence(StorageKey.user_stats.value).save_json(vars(user_stats))


def read_user_stats(user_stats: UserStats) -> None:
    try:
        raw_stats = Persistence(StorageKey.user_stats.value).read_json()
        properties = raw_stats["properties"]
        wish_wit = raw_stats["wish_wit"]
        wish_history = raw_stats["wish_history"]
    except Exception as e:
        return
    user_stats.properties = properties
    user_stats.audit_properties()
    user_stats.num_wish_wits = wish_wit
    user_stats.wish_history = wish_history


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
    banner.shuffle_all()
    read_banner(banner)
    return banner
