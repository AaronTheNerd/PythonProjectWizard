from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional

from merlin.answer import Answer
from merlin.exception import DefaultMissingException


@dataclass
class Question(ABC):
    prompt: str
    default: Optional[str] = field(default=None)

    def validate_raw_input(self, raw_input: str) -> Answer:
        input = self.check_for_default(raw_input)
        return self.validate_or_default(input)

    @abstractmethod
    def validate_or_default(self, input: str) -> Answer:
        ...

    def check_for_default(self, raw_input: str) -> str:
        if raw_input == "":
            return self.apply_default()
        return raw_input

    def apply_default(self) -> str:
        if self.default is None:
            raise DefaultMissingException("Please enter a value")
        return self.default
    