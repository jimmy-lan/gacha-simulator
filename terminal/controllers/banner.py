from random import Random
from typing import Dict, List

from models.banner_reward import BannerReward
from models.reward_rarity import RewardRarity


class Banner:
    # A dictionary mapping reward rarity to an array of rewards.
    # A given reward may repeat multiple times in the list based on the weight of the reward.
    item_pool: Dict[RewardRarity.value, List[BannerReward]]
    # Weight of each rarity category.
    rarity_weights: Dict[RewardRarity.value, float]
    total_rarity_weight: float
    # Number of draws that guarantees
    pity_draws: int
    random: Random

    def __init__(self, rarity_weights: Dict[RewardRarity.value, float]):
        self.item_pool = {}
        self.random = Random()
        self.rarity_weights = rarity_weights
        self.total_rarity_weight = sum(rarity_weights.values())

    def add_reward(self, reward: BannerReward) -> None:
        if reward.rarity not in self.item_pool:
            self.item_pool[reward.rarity] = []
        self.item_pool[reward.rarity].extend([reward] * reward.weight)

    def shuffle(self, rarity: RewardRarity.value) -> None:
        if rarity not in self.item_pool:
            return
        self.random.shuffle(self.item_pool[rarity])

    def shuffle_all(self) -> None:
        for rarity in self.item_pool.keys():
            self.shuffle(rarity)
