from dataclasses import dataclass, field
from typing import ClassVar

from python_project_wizard.dialog.dialog import Dialog
from python_project_wizard.project import Project
from python_project_wizard.question.bool_question import BoolQuestion
from python_project_wizard.question.plain_question import PlainQuestion
from python_project_wizard.question.version_question import VersionQuestion
from python_project_wizard.question_suite import QuestionSuite


project_question_suite = QuestionSuite(
    {
        "name": PlainQuestion("What is the name of your Project?"),
        "python_version": VersionQuestion("What version of Python?", default="3.10"),
        "use_black_formatting": BoolQuestion(
            "Add Black formatting to your project?", default="Y"
        ),
        "use_logging": BoolQuestion("Logging?", default="Y"),
        "use_unittest": BoolQuestion("Unit Tests?", default="Y"),
        "use_configs": BoolQuestion("Configs?", default="Y"),
        "use_args": BoolQuestion("Arguments?", default="N"),
    }
)


@dataclass
class ProjectDialog(Dialog[Project]):
    question_suite: ClassVar[QuestionSuite] = field(
        init=False, default=project_question_suite
    )

    def run(self) -> Project:
        project = Project()
        return self.runner.run(project, self.question_suite)
