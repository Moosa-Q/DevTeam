def save_prompt(prompt):
    """Use this function after creating the prompt to save it"""
    with open("prompt.md", "w", encoding="utf-8") as prompt_file:
        prompt_file.write(prompt)