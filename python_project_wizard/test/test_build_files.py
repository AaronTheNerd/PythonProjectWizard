import os
import unittest
import unittest.mock as mock

from python_project_wizard.build_project.build_files import *
from python_project_wizard.project import Project
from python_project_wizard.build_project.get_launch_json_content import *


class BuildFilesTestSuite(unittest.TestCase):
    @mock.patch("builtins.open")
    def test_build_file(self, mocked_open: mock.Mock):
        filepath = os.path.join(os.getcwd(), "file_test1.txt")
        build_file(filepath, "Hello, World")
        call = [mock.call(filepath, "w+")]
        mocked_open.assert_has_calls(call)

    @mock.patch("python_project_wizard.build_project.build_files.build_file")
    def test_build_static(self, mocked_build: mock.Mock):
        project = Project(name="merlin project")
        directories = Directories(os.getcwd(), project)
        build_static_files(project, directories)
        mocked_build.assert_any_call(
            os.path.join(directories.main, "README.md"), "# Merlin Project"
        )

    @mock.patch("python_project_wizard.build_project.build_files.build_file")
    def test_build_launch_json(self, mockec_build: mock.Mock):
        project = Project(name="merlin project")
        directories = Directories(os.getcwd(), project)
        build_launch_json(project, directories)
        mockec_build.assert_any_call(
            os.path.join(directories.dot_vscode, "launch.json"),
            get_launch_json_content(project),
        )
