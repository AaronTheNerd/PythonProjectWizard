import os
import subprocess

from python_project_wizard.build_project.directories import Directories
from python_project_wizard.build_project.file import build_file
from python_project_wizard.project import Project


# 1. Create new folder at CWD (CHECK)
# 2. Create new pipenv in new folder (CHECK)
# 3. Create new source code folder (CHECK)
# 4. Create README.md (CHECK)
# 4.1. Add .vscode folder (CHECK)
# 4.2. Add launch.json file
# 5. Download main.py source code file
# 6. Download any files which user added to project (args, configs, logging, unittest)
# 7. If unittest was added, add a launch.json config for running
# 8. If black formatting was added, pipenv install black and add a launch.json config
# 9. Modify main.py to import and initialize the add-ons
def build_project(project: Project):
    directories = build_directories()
    initialize_pipenv(project, directories)
    build_files(project, directories)


def build_directories(project: Project) -> Directories:
    cwd = os.getcwd()
    directories = Directories(cwd, project)
    directories.build()
    return directories


def initialize_pipenv(project: Project, directories: Directories):
    subprocess.run(
        ["pipenv", "install", "--python", project.python_version], cwd=directories.main
    )


def build_files(project: Project, directories: Directories):
    build_file(os.path.join(directories.main, "README.md"), f"# {project.name}")
