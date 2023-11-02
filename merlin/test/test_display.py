import unittest
import unittest.mock as mock

from merlin.answer import Answer
from merlin.display.console import Console
from merlin.display.display import Display
from merlin.question import Question
from merlin.validator import raw_validator, yes_or_no_validator


class DisplayTestSuite(unittest.TestCase):
    def test_constructor(self):
        self.assertIsInstance(Console("> "), Display)

    def test_prompt_return_type(self):
        with mock.patch("builtins.input", return_value="Aaron"):
            self.assertIsInstance(Console("").get_answer_from_user(Question("Name?", raw_validator)), Answer)

    def test_prompt_return_value(self):
        test_name = "Aaron"
        with mock.patch("builtins.input", return_value=test_name):
            display = Console("")
            answer = display.get_answer_from_user(Question("Name?", raw_validator))
            self.assertEqual(test_name, answer.value)

    def test_prompt_validator_return_value(self):
        test_input = "Yes"
        with mock.patch("builtins.input", return_value=test_input):
            display = Console("")
            answer = display.get_answer_from_user(Question("Do you use VSCode?", yes_or_no_validator))
            self.assertIsInstance(answer.value, bool)
            self.assertTrue(answer.value)

    def test_two_prompts_on_error(self):
        test_inputs = ["huh", "N"]
        with mock.patch("builtins.input", side_effect=test_inputs):
            display = Console("")
            answer = display.get_answer_from_user(Question("Do you use VSCode?", yes_or_no_validator))
            self.assertIsInstance(answer.value, bool)
            self.assertFalse(answer.value)