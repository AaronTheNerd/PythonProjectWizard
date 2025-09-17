from dataclasses import dataclass
from abc import ABC, abstractmethod

from python_project_wizard.file import File


@dataclass
class FileStore(ABC):
    @abstractmethod
    def get_files(self) -> dict[str, File]:
        ...
