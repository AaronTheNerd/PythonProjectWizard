from merlin.answer import Answer
from merlin.question.question import Question


class PlainQuestion(Question):
    def validate_or_default(self, raw_input: str) -> Answer:
        return Answer(raw_input)