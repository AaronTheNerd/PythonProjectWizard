import os

from dataclasses import dataclass

from python_project_wizard.file_store.file_store import FileStore


@dataclass
class FolderStore(FileStore):
    templates_directory_path: str = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "..", "templates"
    )

    def get_file_content(self, filename: str) -> str:
        self.validate_directory_path()
        filepath = os.path.join(self.templates_directory_path, filename)
        self.validate_filepath(filepath)
        return self.get_filepath_content(filepath)

    def validate_directory_path(self) -> None:
        if not os.path.exists(self.templates_directory_path):
            raise InvalidDirectory()
        if not os.path.isdir(self.templates_directory_path):
            raise InvalidDirectory()

    def validate_filepath(self, filepath: str) -> None:
        if not os.path.isfile(filepath):
            raise InvalidFilePath()

    def get_filepath_content(self, filepath: str) -> str:
        with open(filepath) as file:
            return file.read()


class InvalidDirectory(Exception):
    ...

class InvalidFilePath(Exception):
    ...
