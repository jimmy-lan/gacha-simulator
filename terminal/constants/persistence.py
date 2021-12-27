import os

DEFAULT_STORAGE_FOLDER_NAME = "storage"
DEFAULT_STORAGE_FOLDER_PATH = os.path.join(os.path.join("..", os.path.dirname(os.path.realpath(__file__))),
                                           DEFAULT_STORAGE_FOLDER_NAME)
