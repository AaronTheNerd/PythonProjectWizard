from abc import ABC, abstractmethod

from merlin.answer import Answer
from merlin.question import Question


class Display(ABC):
    @abstractmethod
    def get_answer_from_user(self, question: Question) -> Answer:
        ...