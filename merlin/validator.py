from typing import Callable
from merlin.answer import Answer

Validator = Callable[[str], Answer]

def name_validator(raw_input: str) -> Answer:
    return Answer()