from models.reward_rarity import RewardRarity

# Determines the weight of each rarity item in the banner.
RARITY_WEIGHTS = {
    RewardRarity.common.value: 60,
    RewardRarity.rare.value: 30,
    RewardRarity.super_rare.value: 9.4,
    RewardRarity.epic.value: 0.6
}

# Determine the maximum number of draws (wishes) needed to get an item of
# the corresponding rarity.
PITY_MAX_DRAW = {
    RewardRarity.epic.value: 90,
    RewardRarity.super_rare.value: 10
}
