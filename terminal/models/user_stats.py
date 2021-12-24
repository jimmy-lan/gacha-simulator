from typing import Dict, List

from models.banner_reward import BannerReward
from models.item_name import ItemName


class UserStats:
    # Mapping item name to quantities.
    properties: Dict[ItemName, float]
    wish_history: List[BannerReward]
