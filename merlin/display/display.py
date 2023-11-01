from abc import ABC, abstractmethod
from merlin.question import Question
from merlin.answer import Answer


class Display(ABC):
    @abstractmethod
    def get_answer_from_user(self, question: Question) -> Answer:
        ...