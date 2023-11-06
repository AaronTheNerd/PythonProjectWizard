#!/home/aaronthenerd/.local/share/virtualenvs/Merlin-NowmQrlJ/bin/python3.10

from merlin.dialog.project_dialog import ProjectDialog
from merlin.display.console import Console
from merlin.dialog_runner.synchronous_runner import SyncRunner
from merlin.utils.console_text import ConsoleTextModifier, modify_text


def main():
    # Run dialog
    shell_prompt = (
        modify_text(
            modify_text("Merlin", ConsoleTextModifier.OKBLUE), ConsoleTextModifier.BOLD
        )
        + "$"
    )
    error_prefix = modify_text(
        modify_text("[ERROR]", ConsoleTextModifier.WARNING), ConsoleTextModifier.BOLD
    )
    console = Console(shell_prompt, error_prefix)
    runner = SyncRunner(console)
    dialog = ProjectDialog(runner)
    project = dialog.run()
    print(project)
    # Create everything
    ...


if __name__ == "__main__":
    main()
