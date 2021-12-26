from colorama import Fore

from models.reward_rarity import RewardRarity

RARITY_COLORS = {
    RewardRarity.epic.value: Fore.YELLOW,
    RewardRarity.super_rare.value: Fore.MAGENTA,
    RewardRarity.rare.value: Fore.BLUE,
    RewardRarity.common.value: Fore.GREEN
}
