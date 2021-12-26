from typing import Dict, List

from models.banner_reward import BannerReward
from models.item_name import ItemName


class UserStats:
    # Property used for performing wish on a banner.
    num_wish_wits: int
    # Mapping item name to quantities.
    properties: Dict[str, float]
    wish_history: List[BannerReward]

    def __init__(self):
        self.num_wish_wits = 0
        self.wish_history = []
        self.properties = {}
        self.audit_properties()

    def audit_properties(self):
        item_names = set([item_name.value for item_name in ItemName])
        invalid_keys = []
        for key in self.properties:
            if key not in item_names:
                invalid_keys.append(key)
        for key in invalid_keys:
            del self.properties[key]
        for item_name in item_names:
            if item_name not in self.properties:
                self.properties[item_name] = 0

    def record_wish(self, reward: BannerReward):
        self.wish_history.append(reward)
        self.properties[reward.name] += reward.quantity
