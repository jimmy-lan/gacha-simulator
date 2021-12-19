from typing import Dict, List

from models.item_name import ItemName
from models.reward_rarity import RewardRarity


class Banner:
    # A dictionary mapping reward rarity to an array of items.
    # An item may repeat multiple times in the list based on the weight of the item.
    item_pool: Dict[RewardRarity, List[ItemName]]

    def __init__(self):
        pass
