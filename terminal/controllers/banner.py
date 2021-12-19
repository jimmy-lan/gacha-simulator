import random
from typing import Dict, List

from models.banner_reward import BannerReward
from models.item_name import ItemName
from models.reward_rarity import RewardRarity


class Banner:
    # A dictionary mapping reward rarity to an array of rewards.
    # A given reward may repeat multiple times in the list based on the weight of the reward.
    item_pool: Dict[RewardRarity, List[BannerReward]]

    def __init__(self):
        pass

    def add_reward(self, reward: BannerReward, rarity: RewardRarity = RewardRarity.common) -> None:
        if rarity not in self.item_pool:
            self.item_pool[rarity] = []
        self.item_pool[rarity].extend([reward] * reward.weight)

    def shuffle(self, rarity: RewardRarity) -> None:
        if rarity not in self.item_pool:
            return
        random.shuffle(self.item_pool[rarity])

    def shuffle_all(self) -> None:
        for rarity in self.item_pool.keys():
            self.shuffle(rarity)
