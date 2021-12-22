from models.reward_rarity import RewardRarity

if __name__ == '__main__':
    for rarity in RewardRarity.__reversed__():
        print(rarity.name)
