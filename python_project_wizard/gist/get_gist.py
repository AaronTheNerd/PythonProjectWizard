from typing import Any

import requests

from python_project_wizard.gist.gist import GistFile

main_gist_id = "743ef81b3a1d6c72e6357b883b7778b0"

def get_gist(gist_id: str=main_gist_id) -> dict[str, GistFile]:
    response = requests.get(f"https://api.github.com/gists/{gist_id}")
    return gist_files_from_response(response.json())

def gist_files_from_response(response: dict[str, Any]) -> dict[str, GistFile]:
    files: dict[str, Any] = response["files"]
    return { filename: GistFile(file["content"]) for filename, file in files.items() }
