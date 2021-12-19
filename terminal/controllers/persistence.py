import json
import os
from os import path
from typing import Dict


class Persistence:
    # Key that corresponds with the item being stored.
    key: str
    # Root folder to persist this key.
    root: str

    def __init__(self, key: str, root: str = "storage"):
        self.key = key
        self.root = root
        self.create_root()

    def create_root(self):
        if not path.exists(self.root):
            os.mkdir(self.root)

    def get_path(self) -> str:
        return f"{path.join(self.root, self.key).strip('.')}.json"

    def save_json(self, obj: Dict) -> None:
        """
        Save the given dictionary as json file.
        :param obj: Dictionary to save.
        """
        with open(self.get_path(), "w") as file:
            json.dump(obj, file)

    def read_json(self) -> Dict:
        """
        Read and return a dictionary corresponding to the current key.
        """
        with open(self.get_path(), "r") as file:
            data = json.load(file)
        return data
