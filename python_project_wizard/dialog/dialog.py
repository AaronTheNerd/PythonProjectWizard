from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import ClassVar, Generic, TypeVar

from python_project_wizard.question_suite import QuestionSuite
from python_project_wizard.dialog_runner.dialog_runner import DialogRunner

T = TypeVar("T")


@dataclass
class Dialog(ABC, Generic[T]):
    runner: DialogRunner
    question_suite: ClassVar[QuestionSuite] = field(init=False)

    @abstractmethod
    def run(self) -> T:
        ...
