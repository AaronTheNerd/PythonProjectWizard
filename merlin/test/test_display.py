import unittest
import unittest.mock as mock

from merlin.answer import Answer
from merlin.display.console import Console
from merlin.display.display import Display
from merlin.question import Question


class DisplayTestSuite(unittest.TestCase):
    def test_constructor(self):
        self.assertIsInstance(Console("> "), Display)

    def test_prompt_return_type(self):
        with mock.patch("builtins.input", return_value="Aaron"):
            self.assertIsInstance(Console("").prompt(Question("Name?")), Answer)

    def test_prompt_return_value(self):
        test_name = "Aaron"
        with mock.patch("builtins.input", return_value=test_name):
            display = Console("")
            answer = display.prompt(Question("Name?"))
            self.assertEquals(test_name, answer.value)