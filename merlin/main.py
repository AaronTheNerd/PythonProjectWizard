#!/home/aaronthenerd/.local/share/virtualenvs/Merlin-NowmQrlJ/bin/python3.10

from merlin.dialog.project_dialog import ProjectDialog
from merlin.display.console import Console
from merlin.question.bool_question import BoolQuestion
from merlin.question.plain_question import PlainQuestion
from merlin.question.version_question import VersionQuestion
from merlin.question_suite import QuestionSuite
from merlin.utils.console_text import ConsoleTextModifier, modify_text


def main():
    # Run dialog
    shell_prompt = modify_text(modify_text('Merlin', ConsoleTextModifier.OKBLUE), ConsoleTextModifier.BOLD) + "$"
    error_prefix = modify_text(modify_text("[ERROR]", ConsoleTextModifier.WARNING), ConsoleTextModifier.BOLD)
    console = Console(shell_prompt, error_prefix)
    question_suite = QuestionSuite({
        "name": PlainQuestion("What is the name of your Project?"),
        "python_version": VersionQuestion("What version of Python?", default="3.10"),
        "use_black_formatting": BoolQuestion("Add Black formatting to your project?", default="Y"),
        "use_logging": BoolQuestion("Logging?", default="Y"),
        "use_unittest": BoolQuestion("Unit Tests?", default="Y"),
        "use_configs": BoolQuestion("Configs?", default="Y"),
        "use_args": BoolQuestion("Arguments?", default="N"),
    })
    dialog = ProjectDialog(console, question_suite)
    project = dialog.run()
    print(project)
    # Create everything
    ...

if __name__ == "__main__":
    main()