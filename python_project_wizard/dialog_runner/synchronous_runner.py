from python_project_wizard.dialog_runner.dialog_runner import DialogRunner
from python_project_wizard.question.question import Question
from python_project_wizard.question_suite import QuestionSuite
from python_project_wizard.answer import Answer
from python_project_wizard.utils.set_field import set_field

from typing import Generic, TypeVar

T = TypeVar("T")


class SyncRunner(DialogRunner[T], Generic[T]):
    def run(self, obj: T, suite: QuestionSuite) -> T:
        for field_name, question in suite.field_to_question.items():
            answer = self.prompt_user_until_answer_provided(question)
            obj = set_field(obj, field_name, answer.value)
        return obj

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
