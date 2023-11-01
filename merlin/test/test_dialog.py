import unittest
from dataclasses import dataclass, field

from merlin.dialog.dialog import Dialog
from merlin.dialog.project_dialog import ProjectDialog
from merlin.display.console import Console
from merlin.display.display import Display
from merlin.project import Project
from merlin.question_suite import QuestionSuite


@dataclass
class TestResult:
    name: str = field(init=False)

class TestDialog(Dialog[TestResult]):
    def run(self) -> TestResult:
        return TestResult()

class DialogTestSuite(unittest.TestCase):
    def test_constructor(self):
        self.assertIsInstance(ProjectDialog(Console(""), QuestionSuite({})), Dialog)

    def test_run(self):
        self.assertIsInstance(ProjectDialog(Console(""), QuestionSuite({})).run(), Project)

    def test_set_field(self):
        test_name = "BEANS"
        test_result = TestResult()
        test_result = TestDialog(Console(""), QuestionSuite({})).set_field(test_result, "name", test_name)
        self.assertEqual(test_result.name, test_name)
