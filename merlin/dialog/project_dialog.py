from dataclasses import dataclass, field
from merlin.dialog.dialog import Dialog
from merlin.project import Project

@dataclass
class ProjectDialog(Dialog[Project]):

    def run(self) -> Project:
        return Project()