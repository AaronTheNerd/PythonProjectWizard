from dataclasses import dataclass

from merlin.answer import Answer
from merlin.dialog.dialog import Dialog
from merlin.project import Project
from merlin.question.question import Question


@dataclass
class ProjectDialog(Dialog[Project]):

    def run(self) -> Project:
        project = Project()
        for field_name, question in self.question_suite.field_to_question.items():
            answer = self.prompt_user_until_answer_provided(question)
            project = self.set_field(project, field_name, answer.value)
        return project
    
    def prompt_user_until_answer_provided(self, question: Question) -> Answer:
        answer = None
        while answer is None:
            answer = self.try_to_get_answer(question)
        return answer
    
    def try_to_get_answer(self, question: Question) -> Answer:
        try:
            return self.get_input_from_user(question)
        except Exception as e:
            self.display.display_error(e)
            return None
        
    def get_input_from_user(self, question: Question) -> Answer:
        raw_input = self.display.prompt(question)
        return question.validate_raw_input(raw_input)
