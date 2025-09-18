from dataclasses import dataclass

from python_project_wizard.input.input import Input


@dataclass
class Console:
    prompt_prefix: str = ""
    error_prefix: str = ""
    info_prefix: str = ""

    def prompt(self, input: Input) -> None:
        default_string = self.get_default_string(input)
        question_string = f"{self.prompt_prefix} {input.prompt}{f' {default_string}'}"
        question_string = question_string.strip()
        return print(f"{question_string} ", end="")

    def get_default_string(self, question: Input) -> str:
        return f"[{question.default_value.upper()}]" if question.default_value != "" else ""

    def input(self) -> str:
        return input()

    def error(self, exception: Exception) -> None:
        print(f"{self.error_prefix} {str(exception)}")

    def info(self, message: str) -> None:
        print(f"{self.info_prefix} {message}")
