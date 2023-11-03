import unittest
import unittest.mock as mock

from merlin.answer import Answer
from merlin.display.console import Console
from merlin.display.display import Display
from merlin.question import Question
from merlin.validator import raw_validator, yes_or_no_validator


class DisplayTestSuite(unittest.TestCase):
    def test_constructor(self):
        self.assertIsInstance(Console(), Display)
        self.assertIsInstance(Console(">"), Display)
        self.assertIsInstance(Console(">", "[ERROR]"), Display)

    def test_prompt_return(self):
        test_input = "Aaron"
        with mock.patch("builtins.input", return_value=test_input):
            raw_input = Console().prompt(Question("Name?", raw_validator))
            self.assertIsInstance(raw_input, str)
            self.assertEqual(raw_input, test_input)
    
    def test_display_error(self):
        test_error_message = "ERROR MESSAGE"
        with mock.patch("builtins.print") as mock_print:
            console = Console()
            console.display_error(Exception(test_error_message))
            mock_print.assert_called()

