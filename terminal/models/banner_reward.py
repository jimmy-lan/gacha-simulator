from models.item_name import ItemName


class BannerReward:
    def __init__(self, name: ItemName, quantity: int = 1, weight: int = 1):
        self.name = name
        self.quantity = quantity
        self.weight = weight
