from dataclasses import dataclass

from merlin.answer import Answer
from merlin.display.display import Display
from merlin.question import Question


@dataclass
class Console(Display):
    shell_prompt: str

    def prompt(self, question: Question) -> Answer:
        return Answer(input(question.prompt))