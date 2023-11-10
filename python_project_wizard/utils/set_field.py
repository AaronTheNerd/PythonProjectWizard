from typing import TypeVar, Any

T = TypeVar("T")


def set_field(object: T, field: str, value: Any) -> T:
    object.__dict__[field] = value
    return object
