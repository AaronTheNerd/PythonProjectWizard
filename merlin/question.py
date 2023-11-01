from dataclasses import dataclass, field
from typing import Optional
from merlin.validator import Validator

@dataclass
class Question:
    prompt: str
    validator: Optional[Validator] = field(default=None)
