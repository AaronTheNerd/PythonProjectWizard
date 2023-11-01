from dataclasses import dataclass

from merlin.validator import Validator


@dataclass
class Question:
    prompt: str
    validator: Validator
