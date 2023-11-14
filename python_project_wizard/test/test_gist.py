import unittest
import unittest.mock as mock

from python_project_wizard.gist.gist import *
from python_project_wizard.gist.get_gist import *

class GistTestSuite(unittest.TestCase):
    def test_gist_file(self):
        file = GistFile("# Test content")
        self.assertIsInstance(file, GistFile)
        self.assertIsInstance(file.content, str)
        self.assertEqual(file.content, "# Test content")

    def test_get_gist(self):
        gist_id = "d01cc283131161adb06eb844a01217ab"
        gist = get_gist(gist_id)
        self.assertIsInstance(gist, dict)
        self.assertIsInstance(gist["test.py"], GistFile)
        self.assertEqual(gist["test.py"].content, "# Test content")

    def test_get_main_gist(self):
        gist = get_gist()
        self.assertIn("args.py", gist.keys())
        self.assertIn("configs.json", gist.keys())
        self.assertIn("configs.py", gist.keys())
        self.assertIn("log.py", gist.keys())
        self.assertIn("logging.conf", gist.keys())
        self.assertIn("main.py", gist.keys())