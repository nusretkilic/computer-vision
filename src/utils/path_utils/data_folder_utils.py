# data_folder_utils.py
from pathlib import Path
from src.utils.path_utils.custom_path_utils import CustomPathUtils

class DataFolderUtils(CustomPathUtils):

    def get_path_as_url(self):
        project_root = Path(__file__).resolve().parent.parent.parent.parent
        data_dir = project_root / "data"
        return str(data_dir)
