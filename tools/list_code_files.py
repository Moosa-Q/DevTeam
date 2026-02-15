def list_code_files(project_folder):
    """Use this function to get the code files"""
    import os
    files = os.listdir(project_folder)
    return files