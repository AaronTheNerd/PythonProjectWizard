from python_project_wizard.build_project.directories import Directories
from python_project_wizard.build_project.file_builder import FileBuilder
from python_project_wizard.build_project.file_formatter import FileFormatter
from python_project_wizard.build_project.pipenv_builder import PipenvBuilder
from python_project_wizard.build_project.project_builder import ProjectBuilder
from python_project_wizard.dialog.console_dialog import ConsoleDialog
from python_project_wizard.file_store.folder_store import FolderStore
from python_project_wizard.input.bool_input import BoolInput
from python_project_wizard.input.input import Input
from python_project_wizard.console.console import Console
from python_project_wizard.console.console_text import ConsoleTextModifier, modify_text
from python_project_wizard.input.text_input import TextInput
from python_project_wizard.input.version_input import VersionInput
from python_project_wizard.project import Project


def create_main_console() -> Console:
    shell_prompt = f"{modify_text('Merlin', [ConsoleTextModifier.OKBLUE, ConsoleTextModifier.BOLD])}$"
    error_prefix = modify_text(
        "[ERROR]", [ConsoleTextModifier.WARNING, ConsoleTextModifier.BOLD]
    )
    message_prefix = modify_text("[INFO]", [ConsoleTextModifier.BOLD])
    return Console(shell_prompt, error_prefix, message_prefix)


def create_project_inputs() -> list[Input]: 
    return [
        TextInput(id="name", prompt="What is the name of your Project?"),
        VersionInput(id="python_version", prompt="What version of Python?", default_value="3.10"),
        BoolInput(id="use_black_formatting", prompt="Add Black formatting?", default_value="Y"),
        BoolInput(id="use_logging", prompt="Add logging?", default_value="Y"),
        BoolInput(id="use_unittest", prompt="Add Unit Tests?", default_value="Y"),
        BoolInput(id="use_configs", prompt="Add configs?", default_value="Y"),
        BoolInput(id="use_args", prompt="Add arguments?", default_value="N"),
        BoolInput(id="use_publishing", prompt="Add publishing?", default_value="N"),
    ]


def main():
    dialog = ConsoleDialog(create_main_console())
    project_kwargs = dialog.display_inputs(create_project_inputs())
    project = Project(**project_kwargs)
    builder = ProjectBuilder(project, dialog, FolderStore(), FileFormatter(project), FileBuilder(Directories(project)), PipenvBuilder(project, Directories(project)))
    builder.build()


if __name__ == "__main__":
    main()
