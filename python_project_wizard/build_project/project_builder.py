from dataclasses import dataclass

from python_project_wizard.build_project.file_builder import FileBuilder
from python_project_wizard.build_project.file_formatter import FileFormatter
from python_project_wizard.build_project.pipenv_builder import PipenvBuilder
from python_project_wizard.dialog.dialog import Dialog
from python_project_wizard.file_store.file_store import FileStore
from python_project_wizard.project import Project


@dataclass
class ProjectBuilder:
    project: Project
    dialog: Dialog
    file_store: FileStore
    file_formatter: FileFormatter
    file_builder: FileBuilder
    pipenv_builder: PipenvBuilder

    def build(self) -> None:
        self.build_files()
        self.pipenv_builder.build()

    def build_files(self) -> None:
        requested_files = self.project.get_files()
        for file in requested_files:
            file.content = self.file_store.get_file_content(file.filename)
            file.content = self.file_formatter.format_file(file.content)
            self.file_builder.build(file)
