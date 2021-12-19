import json
from os import path
from typing import Dict

STORAGE_ROOT = "storage"


class Persistence:
    key: str

    def __init__(self, key: str):
        self.key = key

    def get_path(self) -> str:
        return f"{path.join(STORAGE_ROOT, self.key).strip('.')}.json"

    def save_json(self, obj: Dict) -> None:
        with open(self.get_path(), "w") as file:
            json.dump(obj, file)

    def read_json(self) -> Dict:
        with open(self.get_path(), "r") as file:
            data = json.load(file)
        return data
