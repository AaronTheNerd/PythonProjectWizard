from dataclasses import dataclass, field

@dataclass(slots=True)
class Project:
    name: str = field(init=False)

