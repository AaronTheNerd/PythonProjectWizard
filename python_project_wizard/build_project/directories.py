import os

from python_project_wizard.project import Project


class Directories:
    def __init__(self, cwd: str, project: Project):
        self.main = os.path.join(cwd, self.main_directory(project.name))
        self.source = os.path.join(self.main, self.source_directory(project.name))
        self.dot_vscode = os.path.join(self.main, ".vscode")
        self.build()

    @staticmethod
    def main_directory(name: str) -> str:
        name = name.title()
        words = name.split()
        return "".join(words)

    @staticmethod
    def source_directory(name: str) -> str:
        name = name.lower()
        words = name.split()
        return "_".join(words)

    def build(self) -> None:
        self.make_dir(self.main)
        self.make_dir(self.source)
        self.make_dir(self.dot_vscode)

    @staticmethod
    def make_dir(path: str) -> None:
        if not os.path.exists(path):
            os.mkdir(path)
