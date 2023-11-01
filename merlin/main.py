#!/home/aaronthenerd/.local/share/virtualenvs/Merlin-NowmQrlJ/bin/python3.10

from merlin.dialog.project_dialog import ProjectDialog
from merlin.display.console import Console
from merlin.question import Question
from merlin.question_suite import QuestionSuite


def main():
    # Run dialog
    console = Console()
    question_suite = QuestionSuite({
        "name": Question("What is the name of your Project?")
    })
    dialog = ProjectDialog(console, question_suite)
    project = dialog.run()
    # Create everything
    ...

if __name__ == "__main__":
    main()