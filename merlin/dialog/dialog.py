from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from merlin.display.display import Display
from merlin.question_suite import QuestionSuite

T = TypeVar("T")

@dataclass
class Dialog(ABC, Generic[T]):
    display: Display
    question_suite: QuestionSuite

    @abstractmethod
    def run(self) -> T:
        ...

    def set_field(self, object: T, field: str, value: Any) -> T:
        object.__dict__[field] = value
        return object
