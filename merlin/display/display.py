from abc import ABC, abstractmethod
from merlin.question import Question
from merlin.answer import Answer


class Display(ABC):
    @abstractmethod
    def prompt(self, question: Question) -> Answer:
        ...