def build_file(path: str, content: str):
    with open(path, "w+") as file:
        file.write(content)
