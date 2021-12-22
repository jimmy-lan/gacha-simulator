from controllers.banner import Banner
from models.banner_reward import BannerReward
from models.item_name import ItemName
from models.reward_rarity import RewardRarity

if __name__ == '__main__':
    banner = Banner({
        RewardRarity.common.value: 45,
        RewardRarity.rare.value: 35,
        RewardRarity.super_rare.value: 15,
        RewardRarity.epic.value: 5
    })
    banner.pity_max_draw = {
        RewardRarity.epic.value: 60,
        RewardRarity.super_rare.value: 10
    }
    banner.pity_threshold = {
        RewardRarity.epic.value: 39,
        RewardRarity.super_rare.value: 8
    }
    banner.add_reward(BannerReward(ItemName.points, quantity=60, weight=80, rarity=RewardRarity.common.value))
    banner.add_reward(BannerReward(ItemName.points, quantity=90, weight=20, rarity=RewardRarity.common.value))
    banner.add_reward(BannerReward(ItemName.points, quantity=150, weight=50, rarity=RewardRarity.rare.value))
    banner.add_reward(BannerReward(ItemName.points, quantity=180, weight=30, rarity=RewardRarity.rare.value))
    banner.add_reward(BannerReward(ItemName.points, quantity=210, weight=20, rarity=RewardRarity.rare.value))
    banner.add_reward(BannerReward(ItemName.points, quantity=500, weight=100, rarity=RewardRarity.super_rare.value))
    banner.add_reward(BannerReward(ItemName.points, quantity=2888, weight=100, rarity=RewardRarity.epic.value))

    for i in range(10):
        print(banner.wish())
