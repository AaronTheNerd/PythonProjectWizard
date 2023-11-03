import re

from merlin.answer import Answer
from merlin.question.question import Question


class BoolQuestion(Question):
    def validate_input_or_default(self, raw_input: str) -> Answer:
        true_input = re.match("^y", raw_input, re.IGNORECASE)
        if true_input: return Answer(True)
        false_input = re.match("^n", raw_input, re.IGNORECASE)
        if false_input: return Answer(False)
        raise ValueError(f"Unexpected value received: `{raw_input}`.")