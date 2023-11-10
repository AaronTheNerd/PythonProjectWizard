from dataclasses import dataclass

from python_project_wizard.display.display import Display
from python_project_wizard.question.question import Question


@dataclass
class Console(Display):
    shell_prompt: str = ""
    error_prefix: str = ""

    def prompt(self, question: Question) -> str:
        default_string = self.get_default_string(question)
        return input(f"{self.shell_prompt} {question.prompt}{f' {default_string}'} ")

    def display_error(self, exception: Exception) -> None:
        print(f"{self.error_prefix} {str(exception)}")

    def get_default_string(self, question: Question) -> str:
        return f"[{question.default.upper()}]" if question.default is not None else ""
