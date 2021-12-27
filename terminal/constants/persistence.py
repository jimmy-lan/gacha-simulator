import os
from pathlib import Path

DEFAULT_STORAGE_FOLDER_NAME = "storage"
DEFAULT_STORAGE_FOLDER_PATH = os.path.join(Path(os.path.realpath(__file__)).parent.parent.absolute(),
                                           DEFAULT_STORAGE_FOLDER_NAME)
