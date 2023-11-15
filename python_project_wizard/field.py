from dataclasses import field
from typing import TypeVar, Any

from python_project_wizard.question.question import Question

T = TypeVar("T")


def set_field(object: T, field: str, value: Any) -> T:
    object.__dict__[field] = value
    return object


def question_field(question: Question):
    return field(default=None, metadata={"question": question}, kw_only=True)
