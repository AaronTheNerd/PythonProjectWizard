from python_project_wizard.dialog.project_dialog import ProjectDialog
from python_project_wizard.display.console import Console
from python_project_wizard.dialog_runner.synchronous_runner import SyncRunner
from python_project_wizard.utils.console_text import ConsoleTextModifier, modify_text
from python_project_wizard.build_python_project import build_python_project


def create_main_console():
    shell_prompt = (
        modify_text(
            modify_text("Merlin", ConsoleTextModifier.OKBLUE), ConsoleTextModifier.BOLD
        )
        + "$"
    )
    error_prefix = modify_text(
        modify_text("[ERROR]", ConsoleTextModifier.WARNING), ConsoleTextModifier.BOLD
    )
    return Console(shell_prompt, error_prefix)


def main():
    console = create_main_console()
    dialog = ProjectDialog(SyncRunner(console))
    project = dialog.run()
    build_python_project(project)


if __name__ == "__main__":
    main()
