from dataclasses import dataclass, field

from merlin.answer import Answer
from merlin.dialog.dialog import Dialog
from merlin.project import Project
from merlin.question import Question
from merlin.exception import ValidatorException, DefaultMissingException


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
        raw_input = self.check_for_default(raw_input, question)
        return question.validator(raw_input)

    def check_for_default(self, raw_input: str, question: Question) -> str:
        if raw_input == "":
            return self.apply_default(question)
        return raw_input
    
    def apply_default(self, question: Question) -> str:
        if question.default is None:
            raise DefaultMissingException("Please enter a value")
        return question.default