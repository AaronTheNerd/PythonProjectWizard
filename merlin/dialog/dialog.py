from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import ClassVar, Generic, TypeVar

from merlin.question_suite import QuestionSuite
from merlin.dialog_runner.dialog_runner import DialogRunner

T = TypeVar("T")


@dataclass
class Dialog(ABC, Generic[T]):
    runner: DialogRunner
    question_suite: ClassVar[QuestionSuite] = field(init=False)

    @abstractmethod
    def run(self) -> T:
        ...
