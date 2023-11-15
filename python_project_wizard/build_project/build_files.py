import os

from python_project_wizard.build_project.directories import Directories
from python_project_wizard.project import Project


def build_files(project: Project, directories: Directories):
    build_file(os.path.join(directories.main, "README.md"), f"# {project.name}")


def build_file(path: str, content: str):
    with open(path, "w+") as file:
        file.write(content)
