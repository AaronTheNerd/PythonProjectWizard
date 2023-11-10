import unittest
import unittest.mock as mock
from dataclasses import dataclass, field

from python_project_wizard.dialog.project_dialog import ProjectDialog
from python_project_wizard.display.display import Display
from python_project_wizard.exception import DefaultMissingException
from python_project_wizard.question.bool_question import BoolQuestion
from python_project_wizard.question.plain_question import PlainQuestion
from python_project_wizard.question.question import Question
from python_project_wizard.question_suite import QuestionSuite
from python_project_wizard.display.console import Console
from python_project_wizard.dialog_runner.synchronous_runner import SyncRunner
from python_project_wizard.dialog_runner.dialog_runner import DialogRunner
from python_project_wizard.project import Project


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


class DialogRunnerTestSuite(unittest.TestCase):
    def test_constructor(self):
        self.assertIsInstance(SyncRunner(Console()), DialogRunner)

    def test_get_answer_validator_return_value(self):
        test_input = "Yes"
        display = Console()
        runner = SyncRunner(display)
        with mock.patch("builtins.input", return_value=test_input):
            answer = runner.prompt_user_until_answer_provided(
                BoolQuestion("Do you use VSCode?")
            )
            self.assertIsInstance(answer.value, bool)
            self.assertTrue(answer.value)

    def test_get_answer_two_prompts_on_error(self):
        test_inputs = ["huh", "N"]
        display = Console()
        runner = SyncRunner(display)
        with mock.patch("builtins.input", side_effect=test_inputs):
            answer = runner.prompt_user_until_answer_provided(
                BoolQuestion("Do you use VSCode?")
            )
            self.assertIsInstance(answer.value, bool)
            self.assertFalse(answer.value)

    def test_error_on_blank_with_no_default(self):
        test_inputs = ["", "Merlin"]
        display = Console()
        runner = SyncRunner(display)
        with mock.patch("builtins.input", side_effect=test_inputs):
            answer = runner.prompt_user_until_answer_provided(PlainQuestion("Name?"))
            self.assertIsInstance(answer.value, str)
            self.assertEqual(answer.value, "Merlin")

    def test_exceptions_displayed(self):
        test_inputs = [
            "",
            "Merlin",  # Name
            "3.10",  # Version
            "",
            "Y",  # Black formatting
            "huh",
            "Y",  # Logging
            "N",  # Unit test
            "",  # Configs
            "",  # args
        ]
        expected_errors = [DefaultMissingException, DefaultMissingException, ValueError]
        display = ErrorTestDisplay()
        question_suite = QuestionSuite(
            {
                "name": PlainQuestion("Name?"),
                "python_version": PlainQuestion("Version?"),
                "use_black_formatting": BoolQuestion("Black?"),
                "use_logging": BoolQuestion("Logging?"),
                "use_unittest": BoolQuestion("Unit Tests?"),
                "use_configs": BoolQuestion("Configs?", "Y"),
                "use_args": BoolQuestion("Arguments?", "N"),
            }
        )
        runner = SyncRunner(display)
        with mock.patch("builtins.input", side_effect=test_inputs):
            runner.run(Project(), question_suite)
            self.assertEqual(len(expected_errors), len(display.errors))
            for i in range(len(expected_errors)):
                self.assertIsInstance(display.errors[i], expected_errors[i])
