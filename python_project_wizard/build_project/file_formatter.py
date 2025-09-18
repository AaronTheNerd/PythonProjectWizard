from dataclasses import dataclass
import re

from python_project_wizard.build_project.name import source_directory
from python_project_wizard.project import Project


@dataclass
class FileFormatter:
    project: Project

    def format_file(self, content: str) -> str:
        content = self.remove_unnecessary_sections(content)
        content = self.add_project_fields(content)
        return content


    def remove_unnecessary_sections(self, content: str) -> str:
        for fieldname, value in vars(self.project).items():
            template_pattern = f'"""ppw: {fieldname}-(.*?)"""'
            replace_string = r"\1" if value else ""
            content = re.sub(template_pattern, replace_string, content, flags=re.DOTALL)
        return content


    def add_project_fields(self, content: str) -> str:
        content = re.sub("{project_source}", source_directory(self.project.name.value), content)
        content = re.sub("{project_title}", self.project.name.value.title(), content)
        content = re.sub("{python_version}", self.project.python_version.value, content)
        return content
