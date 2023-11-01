import unittest
from typing import Callable

from merlin.validator import name_validator

class ValidatorTestSuite(unittest.TestCase):
    def test_name_validator_callable(self):
        self.assertIsInstance(name_validator, Callable)