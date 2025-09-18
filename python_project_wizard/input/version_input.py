from dataclasses import dataclass, field

from python_project_wizard.input.input import Input


def valid_versions_factory() -> list[str]:
    return ["3.10", "3.11", "3.12"]


@dataclass
class VersionInput(Input[str]):
    valid_versions: list[str] = field(default_factory=valid_versions_factory)
    
    def valid(self, value: str):
        return value in self.valid_versions
    
    def parse(self, value: str):
        return value