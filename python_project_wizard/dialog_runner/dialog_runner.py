from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar

from python_project_wizard.display.display import Display
from python_project_wizard.question_suite import QuestionSuite

T = TypeVar("T")


@dataclass
class DialogRunner(ABC, Generic[T]):
    display: Display

    @abstractmethod
    def run(self, obj: T, suite: QuestionSuite) -> T:
        ...
