from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from python_project_wizard.input.input import Input


@dataclass
class Dialog(ABC):

    @abstractmethod
    def display_inputs(self, inputs: list[Input]) -> dict[str, Any]:
        ...

    @abstractmethod
    def display_build_progress(self, progress: float) -> None:
        ...
