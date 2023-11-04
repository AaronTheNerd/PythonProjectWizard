import unittest

from merlin.question.plain_question import PlainQuestion
from merlin.question_suite import QuestionSuite


class QuestionSuiteTestSuite(unittest.TestCase):
    def test_constructor(self):
        suite = QuestionSuite({"name": PlainQuestion("Name of Project: ")})
        self.assertIsInstance(suite, QuestionSuite)
