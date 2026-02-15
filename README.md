DevTeam — AI-powered Project Automation
======================================

DevTeam is a small Python toolkit and agent pipeline that automates prompt engineering, planning, code generation, and iterative review using the Google ADK-style agent primitives. It provides a lightweight set of helper tools (`tools/`) for reading and saving prompts, creating project folders, and persisting plans and generated code.

Key features
------------
- Iterative prompt generation and critique loop.
- Planner agent that creates a project plan and file list.
- Coder agent that scaffolds project files and saves generated code.
- Critic/refiner loops for prompts and code to ensure quality.
- Small, easy-to-understand helper tools under `tools/` for I/O and file operations.

When to use this repository
---------------------------
- Prototyping AI-assisted project scaffolding and code generation.
- Building an experiment harness around Google ADK/Litellm-style agents.
- Educational examples for multi-agent orchestration and tooling.

Quick architecture overview
---------------------------
- `dev_team/agent.py` — the main pipeline wiring together LlmAgent, LoopAgent, and SequentialAgent instances. The pipeline flows: prompt generation → prompt refinement → planning → code generation → code refinement → congratulation.
- `tools/` — small modules used as tools by agents (e.g., `save_prompt`, `read_prompt`, `create_plan`, `save_code`, `read_code`).
- `prompt.md` and `plan.md` — on-disk artifacts for prompts and plans used by the agents.

Requirements & supported libs
----------------------------
See `pyproject.toml` for declared dependencies. The project expects Python 3.13+ and commonly-used libraries including `fastapi`, `google-adk`, `litellm`, `streamlit`, and `uvicorn`.

Prerequisites
-------------
- Python 3.13 or later.
- API keys / credentials for the model providers you intend to use (for example, environment variables expected by `google-adk` or `litellm`).

Installation
------------
1. Create and activate a virtual environment:

	 ```bash
	 python -m venv .venv
	 .\.venv\Scripts\activate
	 ```

2. Install dependencies (from `pyproject.toml`). Two common options:

	 - Using pip (installs latest published versions shown in `pyproject.toml`):

		 ```bash
		 python -m pip install -r <(python - <<'PY'
import tomllib,sys
print('\n'.join([dep for dep in tomllib.loads(open('pyproject.toml','rb').read())['project']['dependencies']]))
PY
)
		 ```

	 - Or install directly with pip (explicit packages):

		 ```bash
		 python -m pip install fastapi google-adk litellm requests streamlit uvicorn
		 ```

Usage
-----
This repository is designed to be used programmatically with the agent primitives it wires together.

- Run a small tool directly (examples):

	```bash
	python -m tools.read_prompt
	python -m tools.list_code_files
	```

- Use the pipeline programmatically from Python. The pipeline is exposed in `dev_team/agent.py` as `root_agent`.

	Example (interactive / script):

	```python
	from dev_team import agent

	# The exact runtime call depends on the ADK's agent API (check your provider docs).
	# Many ADK agent classes expose `run()` or similar; adapt as needed:
	# agent.root_agent.run()
	```

Files and important modules
---------------------------
- `dev_team/agent.py` — main pipeline wiring for prompt generation, planning, coding, and refinement loops.
- `tools/read_prompt.py`, `tools/save_prompt.py` — prompt persistence helpers.
- `tools/access_plan.py` — create/read plan persisted to `tools/plan.md`.
- `tools/save_code.py`, `tools/read_code.py`, `tools/list_code_files.py` — helpers for saving and inspecting generated code.
- `prompt.md` — working prompt file.
- `tools/plan.md` — planner output.

Development workflow
--------------------
1. Prepare credentials and environment variables for any model provider you will use (for example, `OPENAI_API_KEY` or provider-specific keys required by `google-adk` / `litellm`).
2. Run the prompt generator and refinement loop to create a strong prompt (`prompt.md`).
3. Run the planner to generate `tools/plan.md`.
4. Run the coder agent to scaffold a project folder and files under a target directory.
5. Iterate using the code critic/refiner loop until satisfied.

Testing and formatting
----------------------
- Add tests under a `tests/` directory and use `pytest` for unit tests.
- Use `ruff` / `black` / `isort` for formatting and linting (not included in the repo yet).

Contributing
------------
- Fork the repo and open a pull request with a clear description of changes.
- Keep commits small and add unit tests for new behavior.
- Update `pyproject.toml` when adding or upgrading dependencies.

Security and secrets
--------------------
- Never commit API keys or credentials. Use environment variables or a secrets manager.
- Be careful when running generated code — review generated files before executing.

Suggested next steps (optional)
-------------------------------
- Add a `LICENSE` file.
- Add a `Makefile` or scripts to simplify common tasks like `venv` setup, install, and run.
- Add a `requirements.txt` or Poetry/Flit configuration for reproducible installs.
- Add a small `examples/` folder demonstrating a complete run.

License
-------
Add a `LICENSE` file to choose a license (for example, MIT). If you want, I can add a `LICENSE` file for you.

Contact
-------
For questions or help, open an issue or reach out to the repository owner.
