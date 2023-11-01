import unittest
from merlin.question_suite import QuestionSuite
from merlin.question import Question

class QuestionSuiteTestSuite(unittest.TestCase):
    def test_constructor(self):
        suite = QuestionSuite({
            "name": Question("Name of Project: ")
        })
        self.assertIsInstance(suite, QuestionSuite)
