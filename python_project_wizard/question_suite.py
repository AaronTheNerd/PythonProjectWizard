from dataclasses import dataclass

from python_project_wizard.question.question import Question


@dataclass
class QuestionSuite:
    field_to_question: dict[str, Question]
