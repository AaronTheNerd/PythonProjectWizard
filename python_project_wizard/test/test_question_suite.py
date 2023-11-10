import unittest

from python_project_wizard.question.plain_question import PlainQuestion
from python_project_wizard.question_suite import QuestionSuite


class QuestionSuiteTestSuite(unittest.TestCase):
    def test_constructor(self):
        suite = QuestionSuite({"name": PlainQuestion("Name of Project: ")})
        self.assertIsInstance(suite, QuestionSuite)
