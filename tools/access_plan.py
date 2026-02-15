from pathlib import Path

# Directory where this tool file lives
BASE_DIR = Path(__file__).resolve().parent

# Absolute path to plan.md
PLAN_PATH = BASE_DIR / "plan.md"


def create_plan(plan: str) -> str:
    """
    Save a generated plan to plan.md.

    This function writes the provided plan text to a file named
    'plan.md' located in the same directory as this tool script.

    Args:
        plan (str):
            The full plan content to be written to disk.

    Returns:
        str:
            Confirmation message indicating where the plan was saved.
    """
    with open(PLAN_PATH, "w", encoding="utf-8") as plan_file:
        plan_file.write(plan)

    return f"Plan saved to {PLAN_PATH}"


def read_plan() -> str:
    """
    Read the saved plan from plan.md.

    This function loads and returns the contents of 'plan.md'
    from the same directory as this tool script.

    Returns:
        str:
            The contents of the plan file.

    Raises:
        FileNotFoundError:
            If plan.md does not yet exist.
    """
    with open(PLAN_PATH, "r", encoding="utf-8") as plan_file:
        return plan_file.read()
