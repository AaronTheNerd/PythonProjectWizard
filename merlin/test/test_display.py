import unittest
import unittest.mock as mock
from dataclasses import dataclass

from merlin.display.console import Console
from merlin.display.display import Display
from merlin.question.plain_question import PlainQuestion
from merlin.question.bool_question import BoolQuestion
from merlin.question.question import Question

@dataclass
class DefaultStringTest:
    question: Question
    expected: str

class DisplayTestSuite(unittest.TestCase):
    def test_constructor(self):
        self.assertIsInstance(Console(), Display)
        self.assertIsInstance(Console(">"), Display)
        self.assertIsInstance(Console(">", "[ERROR]"), Display)

    def test_prompt_return(self):
        test_input = "Aaron"
        with mock.patch("builtins.input", return_value=test_input):
            raw_input = Console().prompt(PlainQuestion("Name?"))
            self.assertIsInstance(raw_input, str)
            self.assertEqual(raw_input, test_input)
    
    def test_display_error(self):
        test_error_message = "ERROR MESSAGE"
        with mock.patch("builtins.print") as mock_print:
            console = Console()
            console.display_error(Exception(test_error_message))
            mock_print.assert_called()

    def test_default_string(self):
        cases = [
            DefaultStringTest(PlainQuestion(""), ""),
            DefaultStringTest(PlainQuestion("", "3.10"), "[3.10]"),
            DefaultStringTest(BoolQuestion(""), ""),
            DefaultStringTest(BoolQuestion("", "y"), "[Y]"),
            DefaultStringTest(BoolQuestion("", "n"), "[N]"),
        ]
        display = Console()
        for case in cases:
            self.assertEqual(display.get_default_string(case.question), case.expected)
