# PyProject

This is my personal Python project template. 
The idea is to create repositories from this template will provide me a boilerplate
for new Python projects.

## Structure
```
.
├── configs.ini
├── LICENSE
├── MANIFEST.in
├── pyproject.toml
├── README.md
├── setup.py
└── src
    └── pyproject
        ├── __init__.py
        ├── __main__.py
        ├── main.py
        ├── __pycache__
        │   └── version.cpython-39.pyc
        ├── tests
        │   ├── __init__.py
        │   └── run.py
        ├── utils
        │   ├── decorators.py
        │   ├── __init__.py
        │   ├── logs.py
        │   ├── project.py
        │   └── unittest_tester.py
        └── version.py
```

## Which files to change?

The following files has the name of the project (PyProject) hardcoded.
- `configs.ini`
- `src/pyproject/main.py`
- `src/pyproject/tests/run.py`

To list files matching case-insensitive `pyproject`, run:
```
grep -iFl "pyproject" --exclude-dir=.git --exclude-dir=__pycache__ -r .
```
