def get_prompt():
    """Use this function to read the completed prompt"""
    with open("../prompt.md", "r", encoding="utf-8") as prompt_file:
        prompt = prompt_file.read()
    return prompt