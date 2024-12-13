#custom_path_utils.py
from abc import ABC, abstractmethod

class CustomPathUtils(ABC):

    @abstractmethod
    def get_path_as_url(self):
        pass
