from dataclasses import dataclass
from typing import Any

from python_project_wizard.dialog.dialog import Dialog
from python_project_wizard.console.console import Console
from python_project_wizard.input.input import Input


@dataclass
class ConsoleDialog(Dialog):
    console: Console

    def display_inputs(self, inputs: list[Input]) -> dict[str, Any]:
        for input in inputs:
            self.display_input_until_answered(input)
        return self.process_inputs(inputs)

    def display_build_progress(self, progress):
        return super().display_build_progress(progress)
    
    def display_input_until_answered(self, input: Input) -> None:
        while input.value is None:
            self.console.prompt(input)
            self.receive_input(input)

    def receive_input(self, input: Input) -> None:
        input.value = raw_input = self.console.input()
        if input.value is None:
            self.console.error(f"Unexpected input: {raw_input}")

    def process_inputs(self, inputs: list[Input]) -> dict[str, Any]:
        return {input.id: input.value for input in inputs}
