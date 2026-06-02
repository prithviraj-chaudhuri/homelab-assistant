# Homelab Assistant
A small collection of agents and tools for inspecting and managing homelab infrastructure.

## Development

- Create and activate a virtual environment (requires Python >= 3.13):

```bash
python -m venv .venv
source .venv/bin/activate
```

- Install the project in editable mode:

```bash
pip install -e .
```

- Start the development server (uses the Makefile):

```bash
make
# or run the underlying command directly
langgraph dev
```

For additional commands, see the `Makefile` and `pyproject.toml`.
