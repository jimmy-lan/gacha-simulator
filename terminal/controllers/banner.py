from random import Random
from typing import Dict, List, Optional

from models.banner_reward import BannerReward
from models.reward_rarity import RewardRarity


class Banner:
    # A dictionary mapping reward rarity to an array of rewards.
    # A given reward may repeat multiple times in the list based on the weight of the reward.
    reward_pool: Dict[str, List[BannerReward]]
    # Weight of each rarity category.
    rarity_weights: Dict[str, float]
    total_rarity_weight: float
    # A mapping where keys are reward rarity and value is the maximum
    # number of draws that guarantees this rarity.
    pity_max_draw: Optional[Dict[str, int]]
    # A mapping where keys are reward rarity and value is the number of
    # draws when the weight of a rarity starts to increase.
    pity_threshold: Optional[Dict[str, int]]
    # Number of consecutive draws including the latest draw that does
    # not include a particular rarity item.
    pity_count: Dict[str, int]
    random: Random

    def __init__(self, rarity_weights: Dict[str, float]):
        self.reward_pool = {}
        self.random = Random()
        self.rarity_weights = rarity_weights
        self.total_rarity_weight = sum(rarity_weights.values())
        self.pity_count = {}
        for rarity in RewardRarity:
            self.pity_count[rarity.value] = 0

    def update_pity_count(self, latest_draw_rarity: str):
        for rarity in self.pity_count.keys():
            self.pity_count[rarity] += 1
        self.pity_count[latest_draw_rarity] = 0

    def add_reward(self, reward: BannerReward) -> None:
        if reward.rarity not in self.reward_pool:
            self.reward_pool[reward.rarity] = []
        self.reward_pool[reward.rarity].extend([reward] * reward.weight)

    def shuffle(self, rarity: str) -> None:
        if rarity not in self.reward_pool:
            return
        self.random.shuffle(self.reward_pool[rarity])

    def shuffle_all(self) -> None:
        for rarity in self.reward_pool.keys():
            self.shuffle(rarity)

    def get_weight(self, rarity: str) -> float:
        """
        Get weight (out of self.total_rarity_weight) of a rarity based on self.rarity_weights and
        pity count and defined pity configurations.
        """
        if self.pity_max_draw is None or rarity not in self.pity_max_draw:
            return self.rarity_weights[rarity]
        if self.pity_threshold is None:
            # When no pity threshold is set, default to no probability increase.
            self.pity_threshold = self.pity_max_draw
        if self.pity_count[rarity] <= self.pity_threshold[rarity]:
            return self.rarity_weights[rarity]

        num_draws_above_threshold = self.pity_count[rarity] - self.pity_threshold[rarity]
        weight_proportion = \
            num_draws_above_threshold / (self.pity_max_draw[rarity] - self.pity_threshold[rarity])
        return self.rarity_weights[rarity] + \
            weight_proportion * (self.total_rarity_weight - self.rarity_weights[rarity])

    def _determine_rarity(self) -> RewardRarity:
        for rarity in RewardRarity.__reversed__():
            rarity_weight = self.get_weight(rarity.value)
            if self.random.random() < rarity_weight / self.total_rarity_weight:
                return rarity
        return RewardRarity.common

    def _select_from_rarity(self, rarity: RewardRarity) -> BannerReward:
        pool = self.reward_pool[rarity.value]
        item_idx = self.random.randint(0, len(pool) - 1)
        return pool[item_idx]

    def wish(self):
        rarity = self._determine_rarity()
        self.update_pity_count(rarity.value)
        return self._select_from_rarity(rarity)
