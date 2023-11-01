from dataclasses import dataclass
from merlin.question import Question

@dataclass
class QuestionSuite:
    field_to_question: dict[str, Question]