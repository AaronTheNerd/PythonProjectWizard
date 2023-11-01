import unittest

from merlin.question import Question
from merlin.question_suite import QuestionSuite
from merlin.validator import name_validator


class QuestionSuiteTestSuite(unittest.TestCase):
    def test_constructor(self):
        suite = QuestionSuite({
            "name": Question("Name of Project: ", name_validator)
        })
        self.assertIsInstance(suite, QuestionSuite)
