from models.reward_rarity import RewardRarity

# Price of wish wit (unit: point)
WISH_WIT_PRICE = 160
MIN_WISHES = 1
MAX_WISHES = 10

# Determine the weight of each rarity item in the banner.
RARITY_WEIGHTS = {
    RewardRarity.common.value: 62,
    RewardRarity.rare.value: 32.4,
    RewardRarity.super_rare.value: 5,
    RewardRarity.epic.value: 0.6
}

# Determine the maximum number of draws (wishes) needed to get an item of
# the corresponding rarity.
PITY_MAX_DRAW = {
    RewardRarity.epic.value: 90,
    RewardRarity.super_rare.value: 10
}

# Determine the threshold to begin increasing probability of getting the corresponding
# rarity reward. If the current number of wishes (without the corresponding rarity item)
# is less than or equal to the threshold, the probability of drawing an item will be based
# on RARITY_WEIGHTS. If the number of wishes is greater than this threshold, probability of
# drawing this rarity item will eventually increase and reach 100% on PITY_MAX_DRAW.
# When an item of the corresponding rarity is drawn, the count will be reset to zero (0).
PITY_THRESHOLD = {
    RewardRarity.epic.value: 66,
    RewardRarity.super_rare.value: 8
}
