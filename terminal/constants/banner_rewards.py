from models.item_name import ItemName
from models.reward_rarity import RewardRarity

# Values are arrays of tuples in the form `(item name, quantity, weight)`
# The player will spend 160 points for each wish.
BANNER_REWARDS = {
    RewardRarity.common.value: [
        (ItemName.crystals, 10, 2),
        (ItemName.crystals, 12, 3),
        (ItemName.crystals, 15, 5),
        (ItemName.crystals, 18, 2),
        (ItemName.crystals, 20, 1),
        (ItemName.commemorative_coins, 10, 1),
        (ItemName.commemorative_coins, 15, 1),
        (ItemName.commemorative_coins, 20, 1),
        (ItemName.drink_voucher_fragments, 1, 3),
        (ItemName.daily_coins, 20, 2),
        (ItemName.daily_coins, 30, 1),
        (ItemName.points, 60, 2),
        (ItemName.points, 80, 1)
    ],
    RewardRarity.rare.value: [
        (ItemName.crystals, 25, 1),
        (ItemName.crystals, 28, 2),
        (ItemName.crystals, 30, 5),
        (ItemName.crystals, 35, 5),
        (ItemName.crystals, 40, 5),
        (ItemName.commemorative_coins, 30, 3),
        (ItemName.commemorative_coins, 40, 2),
        (ItemName.commemorative_coins, 50, 1),
        (ItemName.daily_coins, 40, 2),
        (ItemName.daily_coins, 50, 2),
        (ItemName.daily_coins, 60, 1),
        (ItemName.drink_voucher_fragments, 2, 1),
        (ItemName.drink_voucher_fragments, 3, 2),
        (ItemName.points, 80, 1),
        (ItemName.points, 100, 1),
        (ItemName.points, 120, 1)
    ],
    RewardRarity.super_rare.value: [
        (ItemName.crystals, 100, 3),
        (ItemName.crystals, 120, 2),
        (ItemName.crystals, 150, 1),
        (ItemName.commemorative_coins, 100, 1),
        (ItemName.commemorative_coins, 120, 1),
        (ItemName.daily_coins, 120, 2),
        (ItemName.daily_coins, 150, 1),
        (ItemName.drink_voucher_fragments, 5, 1),
        (ItemName.drink_voucher_fragments, 8, 1),
        (ItemName.drink_voucher_fragments, 10, 1),
        (ItemName.points, 160, 1),
        (ItemName.points, 200, 2),
    ],
    RewardRarity.epic.value: [
        (ItemName.crystals, 3688, 10),
        (ItemName.commemorative_coins, 3000, 2),
        (ItemName.drink_vouchers, 1, 1),
        (ItemName.daily_coins, 5000, 1),
        (ItemName.points, 6400, 1),
    ]
}