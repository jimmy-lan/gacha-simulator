from models.item_name import ItemName


class BannerReward:
    name: str
    quantity: int
    weight: int

    def __init__(self, name: ItemName, quantity: int = 1, weight: int = 1):
        self.name = name.value
        self.quantity = quantity
        self.weight = weight
