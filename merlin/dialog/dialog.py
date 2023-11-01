from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any
from dataclasses import dataclass, field

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
