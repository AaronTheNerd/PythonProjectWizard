import unittest
from merlin.answer import Answer

class AnswerTestSuite(unittest.TestCase):
    def test_constructor(self):
        self.assertIsInstance(Answer(""), Answer)


