from dataclasses import dataclass
from abc import ABC, abstractmethod

from python_project_wizard.build_project.file import File


@dataclass
class FileStore(ABC):
    @abstractmethod
    def get_file_content(self, filename: str) -> str:
        ...
