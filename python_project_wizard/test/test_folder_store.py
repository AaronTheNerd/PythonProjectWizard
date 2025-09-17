import os
import unittest
import unittest.mock as mock

from python_project_wizard.file_store.file_store import FileStore
from python_project_wizard.file_store.folder_store import FolderStore


class FolderTestSuite(unittest.TestCase):
    def test_default_constructor(self):
        folder_store = FolderStore()
        self.assertIsInstance(folder_store, FileStore)

    def test_main_folder_store(self):
        folder_store = FolderStore()
        files = folder_store.get_files()
        self.assertIn("args.py", files.keys())
        self.assertIn("configs.json", files.keys())
        self.assertIn("configs.py", files.keys())
        self.assertIn("log.py", files.keys())
        self.assertIn("logging.conf", files.keys())
        self.assertIn("main.py", files.keys())

    def test_get_files_return_type(self):
        self.assertIsInstance(FolderStore().get_files(), dict)
