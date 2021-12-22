from random import Random
from typing import Dict, List, Optional

from models.banner_reward import BannerReward
from models.reward_rarity import RewardRarity


class Banner:
    # A dictionary mapping reward rarity to an array of rewards.
    # A given reward may repeat multiple times in the list based on the weight of the reward.
    item_pool: Dict[RewardRarity.value, List[BannerReward]]
    # Weight of each rarity category.
    rarity_weights: Dict[RewardRarity.value, float]
    total_rarity_weight: float
    # A mapping where keys are reward rarity and value is the maximum
    # number of draws that guarantees this rarity. List the highest
    # rarity item first.
    pity_max_draw: Optional[Dict[RewardRarity.value, int]]
    # A mapping where keys are reward rarity and value is the number of
    # draws when the weight of a rarity starts to increase.
    pity_threshold: Optional[Dict[RewardRarity.value, int]]
    # Number of consecutive draws including the latest draw that does
    # not include a particular rarity item.
    pity_count: Dict[RewardRarity.value, int]
    random: Random

    def __init__(self, rarity_weights: Dict[RewardRarity.value, float]):
        self.item_pool = {}
        self.random = Random()
        self.rarity_weights = rarity_weights
        self.total_rarity_weight = sum(rarity_weights.values())
        self.pity_count = {}
        for rarity in RewardRarity:
            self.pity_count[rarity.value] = 0

    def update_pity_count(self, latest_draw_rarity: RewardRarity.value):
        for rarity in self.pity_count.keys():
            self.pity_count[rarity] += 1
        self.pity_count[latest_draw_rarity] = 0

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

    def get_extra_weight(self, rarity: RewardRarity.value):
        """
        Get extra weight (out of self.total_rarity_weight) of a rarity based on
        pity count and defined pity configurations.
        """
        if self.pity_max_draw is None:
            return 0
        if self.pity_threshold is None:
            # When no pity threshold is set, default to no probability increase.
            self.pity_threshold = self.pity_max_draw
        if self.pity_count[rarity] <= self.pity_threshold[rarity]:
            return 0

        num_draws_above_threshold = self.pity_count[rarity] - self.pity_threshold[rarity]
        weight_proportion = \
            num_draws_above_threshold / (self.pity_max_draw[rarity] - self.pity_threshold[rarity])
        return weight_proportion * (self.total_rarity_weight - self.rarity_weights[rarity])
