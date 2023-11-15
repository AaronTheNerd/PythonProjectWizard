from python_project_wizard.question.plain_question import PlainQuestion
from python_project_wizard.question.bool_question import BoolQuestion
from python_project_wizard.question.version_question import VersionQuestion
from python_project_wizard.field import question_field

from dataclasses import dataclass


@dataclass
class Project:
    name: str = question_field(PlainQuestion("What is the name of your Project?"))
    python_version: str = question_field(
        VersionQuestion("What version of Python?", default="3.10"),
    )
    use_black_formatting: bool = question_field(
        BoolQuestion("Add Black formatting?", default="Y"),
    )
    use_logging: bool = question_field(
        BoolQuestion("Add logging?", default="Y"),
    )
    use_unittest: bool = question_field(BoolQuestion("Add Unit Tests?", default="Y"))
    use_configs: bool = question_field(BoolQuestion("Add configs?", default="Y"))
    use_args: bool = question_field(BoolQuestion("Add arguments?", default="N"))
