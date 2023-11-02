from dataclasses import dataclass

from merlin.display.display import Display
from merlin.question import Question


@dataclass
class Console(Display):
    shell_prompt: str

    def prompt(self, question: Question) -> str:
        return input(f"{self.shell_prompt} {question.prompt} ")