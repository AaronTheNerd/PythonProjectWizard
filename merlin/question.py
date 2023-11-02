from dataclasses import dataclass, field
from typing import Optional

from merlin.validator import Validator


@dataclass
class Question:
    prompt: str
    validator: Validator
    default: Optional[str] = field(default=None)