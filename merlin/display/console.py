from dataclasses import dataclass

from merlin.answer import Answer
from merlin.display.display import Display
from merlin.question import Question
from merlin.validator import ValidatorException


@dataclass
class Console(Display):
    shell_prompt: str

    def prompt(self, question: Question) -> Answer:
        answer = None
        while answer is None:
            try:
                raw_input = input(question.prompt)
                answer = question.validator(raw_input)
            except ValidatorException as e:
                ...
        return answer