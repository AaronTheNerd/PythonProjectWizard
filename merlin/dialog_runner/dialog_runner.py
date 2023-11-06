from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar

from merlin.display.display import Display
from merlin.question_suite import QuestionSuite

T = TypeVar("T")

@dataclass
class DialogRunner(ABC, Generic[T]):
    display: Display

    @abstractmethod
    def run(self, obj: T, suite: QuestionSuite) -> T:
        ...
