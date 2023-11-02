import unittest
import unittest.mock as mock
from dataclasses import dataclass, field

from merlin.answer import Answer
from merlin.dialog.dialog import Dialog
from merlin.dialog.project_dialog import ProjectDialog
from merlin.display.console import Console
from merlin.display.display import Display
from merlin.project import Project
from merlin.question import Question
from merlin.question_suite import QuestionSuite
from merlin.validator import raw_validator, yes_or_no_validator


@dataclass
class TestResult:
    name: str = field(init=False)

@dataclass
class TestDisplay(Display):
    def prompt(self, question: Question) -> str:
        return question.prompt

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

    def test_get_answer_validator_return_value(self):
        test_input = "Yes"
        display = Console("")
        suite = QuestionSuite({})
        dialog = ProjectDialog(display, suite)
        with mock.patch("builtins.input", return_value=test_input):
            answer = dialog.get_answer_from_user(Question("Do you use VSCode?", yes_or_no_validator))
            self.assertIsInstance(answer.value, bool)
            self.assertTrue(answer.value)

    def test_get_answer_two_prompts_on_error(self):
        test_inputs = ["huh", "N"]
        display = Console("")
        suite = QuestionSuite({})
        dialog = ProjectDialog(display, suite)
        with mock.patch("builtins.input", side_effect=test_inputs):
            answer = dialog.get_answer_from_user(Question("Do you use VSCode?", yes_or_no_validator))
            self.assertIsInstance(answer.value, bool)
            self.assertFalse(answer.value)

    def test_error_on_blank_with_no_default(self):
        test_inputs = ["", "Merlin"]
        display = Console("")
        suite = QuestionSuite({})
        dialog = ProjectDialog(display, suite)
        with mock.patch("builtins.input", side_effect=test_inputs):
            answer = dialog.get_answer_from_user(Question("Name?", raw_validator))
            self.assertIsInstance(answer.value, str)
            self.assertEqual(answer.value, "Merlin")

    def test_run(self):
        display = TestDisplay()
        question_suite = QuestionSuite({
            "name": Question("Name?", raw_validator),
            "python_version": Question("Version?", raw_validator),
            "use_black_formatting": Question("Black?", raw_validator),
            "use_logging": Question("Logging?", raw_validator),
            "use_unittest": Question("Unit Tests?", raw_validator),
            "use_configs": Question("Configs?", raw_validator),
            "use_args": Question("Arguments?", raw_validator),
        })
        dialog = ProjectDialog(display, question_suite)
        project = dialog.run()
        self.assertEqual(project.name, "Name?")
        self.assertEqual(project.python_version, "Version?")
        self.assertEqual(project.use_black_formatting, "Black?")
        self.assertEqual(project.use_logging, "Logging?")
        self.assertEqual(project.use_unittest, "Unit Tests?")
        self.assertEqual(project.use_configs, "Configs?")
        self.assertEqual(project.use_args, "Arguments?")
