from dataclasses import dataclass
import re

from python_project_wizard.input.input import Input


@dataclass
class BoolInput(Input[bool]):
    def valid(self, value: str) -> bool:
        return re.match("^[ny]", value, re.IGNORECASE)
    
    def parse(self, value: str) -> bool:
        if re.match("^y", value, re.IGNORECASE) is not None:
            return True
        return False
        