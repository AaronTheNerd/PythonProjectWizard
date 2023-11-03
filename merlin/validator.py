import re
from typing import Callable

from merlin.answer import Answer
from merlin.exception import ValidatorException

Validator = Callable[[str], Answer]

def raw_validator(raw_input: str) -> Answer:
    return Answer(raw_input)

def yes_or_no_validator(raw_input: str) -> Answer: 
    true_input = re.match("^y", raw_input, re.IGNORECASE)
    if true_input: return Answer(True)
    false_input = re.match("^n", raw_input, re.IGNORECASE)
    if false_input: return Answer(False)
    raise ValidatorException(f"Unexpected value received: `{raw_input}`.")
