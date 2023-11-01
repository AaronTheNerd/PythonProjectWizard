import unittest

from merlin.question import Question
from merlin.validator import name_validator


class QuestionTestSuite(unittest.TestCase):
    def test_constructor(self):
        self.assertIsInstance(Question(""), Question)

    def test_constructor_with_validator(self):
        self.assertIsInstance(Question("Name?", name_validator), Question)