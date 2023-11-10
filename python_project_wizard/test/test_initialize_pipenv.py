import os
import unittest
import unittest.mock as mock

import subprocess

from python_project_wizard.directories import *
from python_project_wizard.build_python_project import initialize_pipenv


class InitializePipenvTestSuite(unittest.TestCase):
    @mock.patch("subprocess.run")
    def test_initialize_pipenv(self, mocked_run: mock.Mock):
        project = Project()
        project.name = "merlin project"
        project.python_version = "3.10"
        cwd = os.getcwd()
        dirs = Directories(cwd, project)
        initialize_pipenv(project, dirs)
        mocked_run.assert_any_call(["pipenv", "install", "--python", "3.10"], cwd=dirs.main)
