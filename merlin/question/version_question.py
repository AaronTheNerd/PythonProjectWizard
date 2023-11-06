from merlin.answer import Answer
from merlin.question.question import Question


class VersionQuestion(Question):
    valid_versions: list[str] = ["3.10"]

    def validate_input_or_default(self, input: str) -> Answer:
        if input not in self.valid_versions:
            raise ValueError(f"Unexpected Python version received `{input}`")
        return Answer(input)
