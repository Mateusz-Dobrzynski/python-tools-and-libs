# 2. Ensuring code quality with pytest ✅

## Checking out to a relevant commit
```bash
git checkout 4c835b7
```

## Directory structure (simplified)
```
.
├── README.md
├── src
│   ├── __init__.py
│   ├── main.py
├── test
│   ├── __init__.py
│   ├── test_misc.py
│   └── test_users.py
├── pyproject.toml
└── uv.lock
```

- `__init__.py` – for proper imports and tests discovery (see [reference](https://www.geeksforgeeks.org/python/what-is-__init__-py-file-in-python/))

## Running pytest with uv

Install pytest:
```bash
uv add pytest
```

Run tests:
```bash
uv run pytest
```

## Coverage reports
```bash
uv add coverage
```

Running tests and collecting coverage data:

```bash
uv run coverage run -m pytest
```

Have a look around:

```bash
ls -latr
```

Did you notice something new?


Display coverage report:

```
uv run coverage report -m
```

Generate a HTML report:

```
uv run coverage html
```
