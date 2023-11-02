from dataclasses import dataclass, field

from merlin.answer import Answer
from merlin.dialog.dialog import Dialog
from merlin.project import Project
from merlin.question import Question
from merlin.validator import ValidatorException


@dataclass
class ProjectDialog(Dialog[Project]):

    def run(self) -> Project:
        project = Project()
        for field_name, question in self.question_suite.field_to_question.items():
            answer = self.get_answer_from_user(question)
            project = self.set_field(project, field_name, answer.value)
        return project
    
    def get_answer_from_user(self, question: Question) -> Answer:
        answer = None
        while answer is None:
            answer = self._try_to_get_answer(question)
        return answer
    
    def _try_to_get_answer(self, question: Question) -> Answer:
        try:
            raw_input = self.display.prompt(question)
            return question.validator(raw_input)
        except ValidatorException as e:
            ...
            return None