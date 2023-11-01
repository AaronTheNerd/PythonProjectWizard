from dataclasses import dataclass

from merlin.answer import Answer
from merlin.display.display import Display
from merlin.question import Question
from merlin.validator import ValidatorException


@dataclass
class Console(Display):
    shell_prompt: str

    def get_answer_from_user(self, question: Question) -> Answer:
        answer = None
        while answer is None:
            answer = self._try_to_get_answer(question)
        return answer
    
    def _try_to_get_answer(self, question: Question) -> Answer:
        try:
            raw_input = self._prompt(question)
            return question.validator(raw_input)
        except ValidatorException as e:
            ...
            return None
        
    def _prompt(self, question: Question) -> str:
        return input(question.prompt)