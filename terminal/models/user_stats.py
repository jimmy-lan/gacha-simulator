from typing import Dict

from models.item_name import ItemName


class UserStats:
    # Mapping item name to quantities.
    properties: Dict[ItemName, float]
