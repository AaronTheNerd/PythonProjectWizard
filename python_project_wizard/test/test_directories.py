import os
import unittest
import unittest.mock as mock

from python_project_wizard.directories import *
from python_project_wizard.project import Project


class CreateProjectTestSuite(unittest.TestCase):
    def test_project_directory_name(self):
        self.assertEqual("Merlin", Directories.main_directory("Merlin"))
        self.assertEqual("Merlin", Directories.main_directory("merlin"))
        self.assertEqual("MerlinProject", Directories.main_directory("merlin project"))

    def test_project_source_name(self):
        self.assertEqual("merlin", Directories.source_directory("Merlin"))
        self.assertEqual("merlin", Directories.source_directory("merlin"))
        self.assertEqual(
            "merlin_project", Directories.source_directory("merlin project")
        )

    def test_constructor(self):
        project = Project()
        project.name = "merlin project"
        cwd = os.getcwd()
        directories = Directories(cwd, project)
        self.assertEqual(directories.cwd, cwd)
        self.assertEqual(
            directories.main,
            os.path.join(cwd, Directories.main_directory(project.name)),
        )
        self.assertEqual(
            directories.source,
            os.path.join(
                cwd,
                Directories.main_directory(project.name),
                Directories.source_directory(project.name),
            ),
        )
        self.assertEqual(
            directories.dot_vscode,
            os.path.join(cwd, Directories.main_directory(project.name), ".vscode"),
        )

    @mock.patch("os.mkdir")
    def test_build(self, mocked_mkdir: mock.Mock):
        project = Project()
        project.name = "merlin project"
        cwd = os.getcwd()
        directories = Directories(cwd, project)
        directories.build()
        calls = [
            mock.call(os.path.join(cwd, "MerlinProject")),
            mock.call(os.path.join(cwd, "MerlinProject", "merlin_project")),
            mock.call(os.path.join(cwd, "MerlinProject", ".vscode")),
        ]
        mocked_mkdir.assert_has_calls(calls, any_order=True)

    def test_change_cwd(self):
        project = Project()
        project.name = "merlin project"
        original_cwd = os.getcwd()
        directories = Directories(original_cwd, project)
        modified_cwd = ""
        with directories.set_cwd("/"):
            modified_cwd = os.getcwd()
        self.assertEqual(original_cwd, os.getcwd())
        self.assertEqual(modified_cwd, "/")
