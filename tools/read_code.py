def read_code(project_folder, filename):
    """Use this function to """
    with open(f"{project_folder}/{filename}", "r", encoding="utf-8") as code_file:
        code = code_file.read()
        return code