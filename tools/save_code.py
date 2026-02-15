def save_code(project_folder, filename, code):
    """Use this function to save code"""
    with open(f"{project_folder}/{filename}", "w", encoding="utf-8") as code_file:
        code_file.write(code)
