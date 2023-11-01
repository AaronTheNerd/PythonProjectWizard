import unittest
from typing import Callable

from merlin.validator import name_validator, yes_or_no_validator, ValidatorException

class ValidatorTestSuite(unittest.TestCase):
    def test_name_validator_callable(self):
        self.assertIsInstance(name_validator, Callable)

    def test_name_validator(self):
        raw_input = "merlin"
        answer = name_validator(raw_input)
        self.assertEqual(answer.value, raw_input)

    def test_yes_or_no_validator_callable(self):
        self.assertIsInstance(yes_or_no_validator, Callable)

    def test_yes_or_no_validator_true_values(self):
        raw_inputs = ["Y", "y", "Yes", "Yeah", "yes", "yup", "you"]
        for raw_input in raw_inputs:
            answer = yes_or_no_validator(raw_input)
            self.assertTrue(answer.value)

    def test_yes_or_no_validator_false_values(self):
        raw_inputs = ["N", "n", "No", "no", "Nah", "nay"]
        for raw_input in raw_inputs:
            answer = yes_or_no_validator(raw_input)
            self.assertFalse(answer.value)

    def test_yes_or_no_validator_error_values(self):
        raw_inputs = ["maybe", "c", "C", "huh"]
        for raw_input in raw_inputs:
            self.assertRaises(ValidatorException, yes_or_no_validator, raw_input)