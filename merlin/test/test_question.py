import unittest

from merlin.question import Question
from merlin.validator import raw_validator


class QuestionTestSuite(unittest.TestCase):
    def test_constructor(self):
        self.assertIsInstance(Question("Name?", raw_validator), Question)
        self.assertIsInstance(Question("Name?", raw_validator, "Merlin"), Question)
