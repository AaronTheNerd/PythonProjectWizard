from __future__ import annotations
from dataclasses import dataclass, field
from typing import Generic, TypeVar

from python_project_wizard.build_project.file import Destination, File


T = TypeVar('T')

@dataclass
class ProjectField(Generic[T]):
    value: T
    files: list[File] = field(default_factory=list)
    packages: list[str] = field(default_factory=list)

class Project:
    def __init__(
        self,
        name: str,
        python_version: str,
        use_black_formatting: bool,
        use_logging: bool,
        use_unittest: bool,
        use_configs: bool,
        use_args: bool,
        use_publishing: bool,
    ) -> Project:
        self.name: ProjectField[str] = ProjectField[str](
            value=name,
            files=[
                File(filename="main.py", destination=Destination.SOURCE),
                File(filename="README.md", destination=Destination.MAIN),
                File(filename="__init__.py", destination=Destination.SOURCE),
                File(filename="launch.json", destination=Destination.VS_CODE),
            ]
        )
        self.python_version: ProjectField[str] = ProjectField[str](
            value=python_version
        )
        self.use_black_formatting: ProjectField[bool] = ProjectField[bool](
            value=use_black_formatting,
            packages=["black"]
        )
        self.use_logging: ProjectField[bool] = ProjectField[bool](
            value=use_logging,
            files=[
                File(filename="log.py", destination=Destination.SOURCE),
                File(filename="logging.conf", destination=Destination.MAIN),
            ]
        )
        self.use_unittest: ProjectField[bool] = ProjectField[bool](
            value=use_unittest,
            files=[
                File(filename="__init__.py", destination=Destination.TEST),
                File(filename="test_example.py", destination=Destination.TEST),
            ],
        )
        self.use_configs: ProjectField[bool] = ProjectField[bool](
            value=use_configs,
            files=[
                File(filename="configs.py", destination=Destination.SOURCE),
                File(filename="configs.json", destination=Destination.MAIN),
            ]
        )
        self.use_args: ProjectField[bool] = ProjectField[bool](
            value=use_args,
            files=[
                File(filename="args.py", destination=Destination.SOURCE)
            ],
        )
        self.use_publishing: ProjectField[bool] = ProjectField[bool](
            value=use_publishing,
            packages=[
                "setuptools", "build", "wheel", "twine"
            ],
            files=[
                File(filename="pyproject.toml", destination=Destination.MAIN),
                File(filename="setup.py", destination=Destination.MAIN),
                File(filename="__init__.py", destination=Destination.SCRIPTS),
                File(filename="build.py", destination=Destination.SCRIPTS),
                File(filename="clean.py", destination=Destination.SCRIPTS),
                File(filename="publish.py", destination=Destination.SCRIPTS),
                File(filename="utils.py", destination=Destination.SCRIPTS)
            ]
        )

    def get_files(self) -> list[File]:
        result = []
        for field in vars(self).values():
            if field.value:
                result += field.files
        return result
    
    def get_packages(self) -> list[str]:
        result = []
        for field in vars(self).values():
            if field.value:
                result += field.packages
        return result
