import unittest
import unittest.mock as mock
from dataclasses import dataclass, field

from merlin.dialog.dialog import Dialog
from merlin.dialog.project_dialog import ProjectDialog
from merlin.display.console import Console
from merlin.display.display import Display
from merlin.exception import DefaultMissingException
from merlin.project import Project
from merlin.question.bool_question import BoolQuestion
from merlin.question.plain_question import PlainQuestion
from merlin.question.question import Question
from merlin.question_suite import QuestionSuite


@dataclass
class TestResult:
    name: str = field(init=False)

@dataclass
class TestDisplay(Display):
    def prompt(self, question: Question) -> str:
        return question.prompt
    
    def display_error(self, exception: Exception) -> None:
        return
    
@dataclass
class ErrorTestDisplay(Display):
    errors: list[Exception] = field(default_factory=list)

    def prompt(self, question: Question) -> str:
        return input(question.prompt)
    
    def display_error(self, exception: Exception) -> None:
        self.errors.append(exception)

class TestDialog(Dialog[TestResult]):
    def run(self) -> TestResult:
        return TestResult()

class DialogTestSuite(unittest.TestCase):
    def test_constructor(self):
        self.assertIsInstance(ProjectDialog(Console(), QuestionSuite({})), Dialog)

    def test_run(self):
        self.assertIsInstance(ProjectDialog(Console(), QuestionSuite({})).run(), Project)

    def test_set_field(self):
        test_name = "BEANS"
        test_result = TestResult()
        test_result = TestDialog(Console(), QuestionSuite({})).set_field(test_result, "name", test_name)
        self.assertEqual(test_result.name, test_name)

    def test_get_answer_validator_return_value(self):
        test_input = "Yes"
        display = Console()
        suite = QuestionSuite({})
        dialog = ProjectDialog(display, suite)
        with mock.patch("builtins.input", return_value=test_input):
            answer = dialog.prompt_user_until_answer_provided(BoolQuestion("Do you use VSCode?"))
            self.assertIsInstance(answer.value, bool)
            self.assertTrue(answer.value)

    def test_get_answer_two_prompts_on_error(self):
        test_inputs = ["huh", "N"]
        display = Console()
        suite = QuestionSuite({})
        dialog = ProjectDialog(display, suite)
        with mock.patch("builtins.input", side_effect=test_inputs):
            answer = dialog.prompt_user_until_answer_provided(BoolQuestion("Do you use VSCode?"))
            self.assertIsInstance(answer.value, bool)
            self.assertFalse(answer.value)

    def test_error_on_blank_with_no_default(self):
        test_inputs = ["", "Merlin"]
        display = Console()
        suite = QuestionSuite({})
        dialog = ProjectDialog(display, suite)
        with mock.patch("builtins.input", side_effect=test_inputs):
            answer = dialog.prompt_user_until_answer_provided(PlainQuestion("Name?"))
            self.assertIsInstance(answer.value, str)
            self.assertEqual(answer.value, "Merlin")

    def test_run(self):
        display = TestDisplay()
        question_suite = QuestionSuite({
            "name": PlainQuestion("Name?"),
            "python_version": PlainQuestion("Version?"),
            "use_black_formatting": PlainQuestion("Black?"),
            "use_logging": PlainQuestion("Logging?"),
            "use_unittest": PlainQuestion("Unit Tests?"),
            "use_configs": PlainQuestion("Configs?"),
            "use_args": PlainQuestion("Arguments?"),
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

    def test_exceptions_displayed(self):
        test_inputs = [
            "", "Merlin", # Name
            "3.10", # Version
            "", "Y", # Black formatting
            "huh", "Y", # Logging
            "N", # Unit test
            "", # Configs
            "" # args
        ]
        expected_errors = [
            DefaultMissingException, 
            DefaultMissingException, 
            ValueError
        ]
        display = ErrorTestDisplay()
        question_suite = QuestionSuite({
            "name": PlainQuestion("Name?"),
            "python_version": PlainQuestion("Version?"),
            "use_black_formatting": BoolQuestion("Black?"),
            "use_logging": BoolQuestion("Logging?"),
            "use_unittest": BoolQuestion("Unit Tests?"),
            "use_configs": BoolQuestion("Configs?", "Y"),
            "use_args": BoolQuestion("Arguments?", "N"),
        })
        dialog = ProjectDialog(display, question_suite)
        with mock.patch("builtins.input", side_effect=test_inputs):
            dialog.run()
            self.assertEqual(len(expected_errors), len(display.errors))
            for i in range(len(expected_errors)):
                self.assertIsInstance(display.errors[i], expected_errors[i])
