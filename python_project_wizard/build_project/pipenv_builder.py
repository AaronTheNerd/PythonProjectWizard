import subprocess
from dataclasses import dataclass

from python_project_wizard.build_project.directories import Directories
from python_project_wizard.project import Project


@dataclass
class PipenvBuilder:
    project: Project
    directories: Directories

    def build(self) -> None:
        self.initialize()
        self.install_packages()

    def initialize(self) -> None:
        subprocess.run(
            ["pipenv", "install", "--python", self.project.python_version.value], cwd=self.directories.main
        )

    def install_packages(self) -> None:
        packages = self.project.get_packages()
        for package in packages:
            subprocess.run(["pipenv", "install", "-d", package], cwd=self.directories.main)

