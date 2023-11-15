import subprocess

from python_project_wizard.build_project.directories import Directories
from python_project_wizard.project import Project


def initialize_pipenv(project: Project, directories: Directories) -> None:
    subprocess.run(
        ["pipenv", "install", "--python", project.python_version], cwd=directories.main
    )

def install_packages(project: Project, directories: Directories) -> None:
    if project.use_black_formatting:
        install_package(directories.main, "black")

def install_package(cwd: str, package: str) -> None:
    subprocess.run(
        ["pipenv", "install", "-d", package], cwd=cwd
    )