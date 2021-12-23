from models.reward_rarity import RewardRarity

# Determines the weight of each rarity item in the banner.
RARITY_WEIGHTS = {
    RewardRarity.common.value: 60,
    RewardRarity.rare.value: 30,
    RewardRarity.super_rare.value: 9.4,
    RewardRarity.epic.value: 0.6
}
