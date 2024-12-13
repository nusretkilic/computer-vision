import unittest
import sys
from pathlib import Path
from src.utils.path_utils.data_folder_utils import DataFolderUtils
from loguru import logger

class TestDataFolderUtils(unittest.TestCase):

    def test_get_path_as_url(self):

        utils = DataFolderUtils()

        expected_path = str(Path(__file__).resolve().parent.parent / 'data')

        result = utils.get_path_as_url()

        logger.info(f"Expected path: {expected_path} | This is expected path as url")
        logger.info(f"Result path: {result} | This is result path as url")

        self.assertEqual(result, expected_path, "The path returned by get_path_as_url is incorrect")

        logger.info("[green]TEST PASSED[/green]")

if __name__ == '__main__':
    logger.remove()
    logger.add(sys.stdout, level="INFO", format="<green>{message}</green>", colorize=True)

    unittest.main()
