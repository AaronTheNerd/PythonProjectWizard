from dataclasses import dataclass, field

from merlin.dialog.dialog import Dialog
from merlin.project import Project


@dataclass
class ProjectDialog(Dialog[Project]):

    def run(self) -> Project:
        project = Project()
        for field_name, question in self.question_suite.field_to_question.items():
            answer = self.display.get_answer_from_user(question)
            project = self.set_field(project, field_name, answer.value)
        return project