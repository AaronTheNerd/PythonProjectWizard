from dataclasses import dataclass, field
from typing import ClassVar

from merlin.dialog.dialog import Dialog
from merlin.project import Project
from merlin.question.bool_question import BoolQuestion
from merlin.question.plain_question import PlainQuestion
from merlin.question.version_question import VersionQuestion
from merlin.question_suite import QuestionSuite


project_question_suite = QuestionSuite(
    {
        "name": PlainQuestion("What is the name of your Project?"),
        "python_version": VersionQuestion(
            "What version of Python?", default="3.10"
        ),
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
    question_suite: ClassVar[QuestionSuite] = field(init=False, default=project_question_suite)
    

    def run(self) -> Project:
        project = Project()
        return self.runner.run(project, self.question_suite)
