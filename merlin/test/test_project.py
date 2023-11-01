import unittest

from merlin.project import Project


class ProjectTestSuite(unittest.TestCase):
    def test_default_constructor(self):
        self.assertIsInstance(Project(), Project)

    def test_set_name(self):
        project_name = "Merlin"
        project = Project()
        project.name = project_name
        self.assertEqual(project_name, project.name)
