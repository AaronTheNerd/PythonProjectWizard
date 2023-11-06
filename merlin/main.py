#!/home/aaronthenerd/.local/share/virtualenvs/Merlin-NowmQrlJ/bin/python3.10

from merlin.dialog.project_dialog import ProjectDialog
from merlin.display.console import Console
from merlin.dialog_runner.synchronous_runner import SyncRunner
from merlin.utils.console_text import ConsoleTextModifier, modify_text


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
    # Run dialog
    runner = SyncRunner(create_main_console())
    dialog = ProjectDialog(runner)
    project = dialog.run()
    print(project)
    # Create everything
    ...


if __name__ == "__main__":
    main()
