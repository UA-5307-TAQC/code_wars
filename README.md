# code_warr

A Python application for managing a coffee cart.

## Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/UA-5307-TAQC/code_wars.git
   ```
2. **Navigate to the project directory:**
   ```
   cd code_wars
   ```
3. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

5. **Install pre-commit hooks (optional but recommended):**
   ```bash
   pre-commit install
   ```

## Pre-commit (how to run locally)

This repository uses pre-commit hooks for formatting and linting. The hooks are configured to use the project's virtual environment executables (under `env/Scripts/` on Windows). The configuration also points flake8 to `.flake8`, pylint to `.pylintrc`, and black/isort use `pyproject.toml`.

Quick steps (Windows PowerShell):

```powershell
# activate the project's venv (if you created it as `env`):
.\env\Scripts\Activate.ps1

# or if you used the project venv named `venv`:
.\venv\Scripts\Activate.ps1

# install dependencies (ensures pre-commit is available and pinned):
python -m pip install -r requirements.txt

# install git hooks (optional):
pre-commit install

# run all hooks on the repository (useful for CI or before committing):
pre-commit run --all-files
```

Cross-platform note

The local pre-commit hooks are configured to use `python -m <tool>` (for example `python -m black`) so they work on Windows, macOS, and Linux as long as the appropriate virtual environment is activated. This avoids hard-coded venv paths and keeps the setup consistent across platforms.

Notes:
- `pre-commit` is pinned in `requirements.txt` to ensure CI and local runs use the same version.
- Config files: `.flake8`, `.pylintrc`, and `pyproject.toml` are used by the configured hooks.

## Usage
To run the application, use the following command:
```bash
python main.py
```

## License

This project is licensed under the MIT License.
