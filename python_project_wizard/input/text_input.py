from dataclasses import dataclass

from python_project_wizard.input.input import Input


@dataclass
class TextInput(Input[str]):
    def valid(self, value: str) -> bool:
        return len(value) > 0
    
    def parse(self, value: str) -> str:
        return value