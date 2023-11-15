import subprocess

from python_project_wizard.build_project.directories import Directories
from python_project_wizard.project import Project


def initialize_pipenv(project: Project, directories: Directories):
    subprocess.run(
        ["pipenv", "install", "--python", project.python_version], cwd=directories.main
    )
