from controllers.banner import Banner
from controllers.program_context import ProgramContext
from helpers import create_banner
from models.banner_reward import BannerReward
from models.item_name import ItemName
from models.reward_rarity import RewardRarity
from colorama import init

init(autoreset=True)

if __name__ == '__main__':
    ProgramContext.initialize()
    banner = ProgramContext.banner

    count = {
        RewardRarity.epic.value: 0,
        RewardRarity.super_rare.value: 0,
        RewardRarity.rare.value: 0,
        RewardRarity.common.value: 0
    }

    while True:
        sign = input(">>> ")
        if sign == "q":
            break
        elif sign == "s":
            print(count)
            print(banner.pity_count)
        elif sign == "v":
            wish_res = banner.wish()
            count[wish_res.rarity] += 1
            print(wish_res)
            print(f"Epic weight: {banner.get_weight(RewardRarity.epic.value)}, Super rare weight:" +
                  f" {banner.get_weight(RewardRarity.super_rare.value)}, Total weight: {banner.total_rarity_weight}")

        elif sign.isdigit():
            for _ in range(int(sign)):
                wish_res = banner.wish()
                count[wish_res.rarity] += 1
                print(wish_res)

    # epic_count = 0
    # num_epic_draws = 0
    # num_total_draws = 1000000
    # for _ in range(num_total_draws):
    #     wish_res = banner.wish()
    #     epic_count += 1
    #     count[wish_res.rarity] += 1
    #     if wish_res.rarity == RewardRarity.epic.value:
    #         num_epic_draws += 1
    #         if epic_count > 90:
    #             exit()
    #             print("ERR")
    #         epic_count = 0
    #
    # print(count)
    # print(f"avg: {num_total_draws / num_epic_draws}")
