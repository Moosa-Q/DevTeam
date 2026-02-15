def read_prompt():
    """Use this tool to read the contents of the generated prompt"""
    with open("prompt.md", "r", encoding="utf-8") as prompt_file:
        prompt = prompt_file.read()
    return prompt