import unittest

from merlin.question.bool_question import BoolQuestion
from merlin.question.plain_question import PlainQuestion
from merlin.question.question import Question


class QuestionTestSuite(unittest.TestCase):
    def test_constructor(self):
        self.assertIsInstance(PlainQuestion("Name?"), Question)
        self.assertIsInstance(PlainQuestion("Name?", "Merlin"), Question)
        self.assertIsInstance(BoolQuestion("Name?"), Question)
        self.assertIsInstance(BoolQuestion("Name?", "Y"), Question)

    def test_name_validator(self):
        raw_input = "merlin"
        question = PlainQuestion("")
        answer = question.validate_or_default(raw_input)
        self.assertEqual(answer.value, raw_input)

    def test_yes_or_no_validator_true_values(self):
        raw_inputs = ["Y", "y", "Yes", "Yeah", "yes", "yup", "you"]
        question = BoolQuestion("")
        for raw_input in raw_inputs:
            answer = question.validate_or_default(raw_input)
            self.assertTrue(answer.value)

    def test_yes_or_no_validator_false_values(self):
        raw_inputs = ["N", "n", "No", "no", "Nah", "nay"]
        question = BoolQuestion("")
        for raw_input in raw_inputs:
            answer = question.validate_or_default(raw_input)
            self.assertFalse(answer.value)

    def test_yes_or_no_validator_error_values(self):
        raw_inputs = ["maybe", "c", "C", "huh"]
        question = BoolQuestion("")
        for raw_input in raw_inputs:
            self.assertRaises(ValueError, BoolQuestion.validate_or_default, question, raw_input)

    def test_set_value_to_default(self):
        test_input = ""
        question = BoolQuestion("Do you use VSCode?", "Y")
        answer = question.validate_raw_input(test_input)
        self.assertIsInstance(answer.value, bool)
        self.assertTrue(answer.value)
