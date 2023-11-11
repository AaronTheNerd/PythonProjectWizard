import os
import unittest
import unittest.mock as mock

from python_project_wizard.build_project.file import *
from python_project_wizard.project import Project


class FileTestSuite(unittest.TestCase):
    @mock.patch("builtins.open")
    def test_constructor(self, mocked_open: mock.Mock):
        filepath = os.path.join(os.getcwd(), "file_test1.txt")
        build_file(filepath, "Hello, World")
        call = [mock.call(filepath, "w+")]
        mocked_open.assert_has_calls(call)
