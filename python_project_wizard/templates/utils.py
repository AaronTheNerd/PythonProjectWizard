import subprocess
import os

CWD = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")

command_params = {
    "shell": True,
    "cwd": CWD,
    "check": True
}


def build() -> None:
    print("Building...")
    subprocess.run(
        "pipenv run python -m build",
        **command_params
    )


def upgrade_twine() -> None:
    print("Upgrading Twine...")
    subprocess.run(
        "pipenv run python -m pip install --upgrade twine",
        **command_params
    )


def publish() -> None:
    print("Publishing...")
    subprocess.run(
        "twine upload --repository pypi dist/*",
        **command_params
    )


def clean() -> None:
    print("Cleaning...")
    subprocess.run(
        "rm -rf dist *.egg-info **/*.egg-info",
        **command_params
    )
