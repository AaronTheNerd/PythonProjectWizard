from abc import ABC, abstractmethod

from merlin.question import Question


class Display(ABC):
    @abstractmethod
    def prompt(self, question: Question) -> str:
        ...