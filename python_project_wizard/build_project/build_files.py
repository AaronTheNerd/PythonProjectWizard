import os

from python_project_wizard.build_project.directories import Directories
from python_project_wizard.build_project.get_launch_json_content import (
    get_launch_json_content,
)
from python_project_wizard.project import Project


def build_files(project: Project, directories: Directories) -> None:
    build_static_files(project, directories)
    build_launch_json(project, directories)
    build_gist_files(project, directories)


def build_static_files(project: Project, directories: Directories) -> None:
    build_file(os.path.join(directories.main, "README.md"), f"# {project.name.title()}")


def build_launch_json(project: Project, directories: Directories) -> None:
    content = get_launch_json_content(project)
    build_file(os.path.join(directories.dot_vscode, "launch.json"), content)


def build_gist_files(project: Project, directories: Directories) -> None:
    ...


def build_file(path: str, content: str) -> None:
    with open(path, "w+") as file:
        file.write(content)
