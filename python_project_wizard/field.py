from dataclasses import field
from typing import TypeVar, Any

from python_project_wizard.question.question import Question
from python_project_wizard.file import File

T = TypeVar("T")


def set_field(object: T, field: str, value: Any) -> T:
    object.__dict__[field] = value
    return object


def get_field_value(object: Any, field: str) -> Any:
    return object.__dict__[field]


def question_field(
    question: Question, files: list[File] = list(), packages: list[str] = list()
):
    return field(
        default=None,
        metadata={"question": question, "files": files, "packages": packages},
        kw_only=True,
    )
