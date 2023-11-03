#!/home/aaronthenerd/.local/share/virtualenvs/Merlin-NowmQrlJ/bin/python3.10

from merlin.dialog.project_dialog import ProjectDialog
from merlin.display.console import Console
from merlin.question import Question
from merlin.question_suite import QuestionSuite
from merlin.utils.console_text import ConsoleTextModifier, modify_text
from merlin.validator import raw_validator, yes_or_no_validator


def main():
    # Run dialog
    shell_prompt = modify_text(modify_text('Merlin', ConsoleTextModifier.OKBLUE), ConsoleTextModifier.BOLD) + "$"
    error_prefix = modify_text(modify_text("[ERROR]", ConsoleTextModifier.WARNING), ConsoleTextModifier.BOLD)
    console = Console(shell_prompt, error_prefix)
    question_suite = QuestionSuite({
        "name": Question("What is the name of your Project?", raw_validator),
        "python_version": Question("What version of Python?", raw_validator),
        "use_black_formatting": Question("Black?", yes_or_no_validator),
        "use_logging": Question("Logging?", yes_or_no_validator),
        "use_unittest": Question("Unit Tests?", yes_or_no_validator),
        "use_configs": Question("Configs?", yes_or_no_validator),
        "use_args": Question("Arguments?", yes_or_no_validator),
    })
    dialog = ProjectDialog(console, question_suite)
    project = dialog.run()
    print(project)
    # Create everything
    ...

if __name__ == "__main__":
    main()