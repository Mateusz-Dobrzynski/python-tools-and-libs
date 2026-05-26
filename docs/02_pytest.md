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

[Coverage reference](https://coverage.readthedocs.io/en/7.14.0/)

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
- `-a` – show hidden files
- `-l` – use a long listing format
- `-t` – sort by modification time (newest first)
- `-r` – reverse the sort order


Did you notice something new?


Display coverage report:

```
uv run coverage report -m
```

Generate a HTML report:

```
uv run coverage html
```

## pytest fixtures

[Fixtures reference](https://docs.pytest.org/en/7.1.x/how-to/fixtures.html)

Create a new test file and paste the following:

```py
from math import floor
from random import random

import pytest


@pytest.fixture
def database_populated_with_content():
    return {
        "fridges": [{"user": "alice", "content": ["Tomato", "Milk", "Eggs"]}],
        "users": [
            {"username": "alice", "plan": "premium", "credit": floor(random() * 500)}
        ],
    }


def test_fixture_demonstration(database_populated_with_content):
    ...

    assert username == "alice"
```

### Fixture independence

Add and run these tests:

```py
def test_variable_fixture_content(database_populated_with_content):
    content = database_populated_with_content

    credit = content["users"].first()["credit"]

    assert credit < 0


def test_variable_fixture_content_reprise(database_populated_with_content):
    content = database_populated_with_content

    credit = content["users"].first()["credit"]

    assert credit < 0
```

## pytest test selection

Add and execute these tests:

```py
import random
import time


def _perform_sleep(min_seconds: float, max_seconds: float) -> None:
    time.sleep(random.uniform(min_seconds, max_seconds))


def test_quick_alpha():
    _perform_sleep(0.05, 1)


def test_quick_bravo():
    _perform_sleep(0.05, 1)


def test_quick_charlie():
    _perform_sleep(0.05, 1)


def test_slow_alpha():
    _perform_sleep(15, 90)


def test_slow_bravo():
    _perform_sleep(15, 90)
```

Decorate slow tests with `@pytest.mark.slow`
```py
@pytest.mark.slow
def test_example()
```

Run only quick tests with:
```bash
uv run pytest -m "not slow"
```

### Skipping slow tests by default

[Pytest reference](https://docs.pytest.org/en/latest/example/simple.html#control-skipping-of-tests-according-to-command-line-option)

Add this to `test/conftest.py`:

```py
import pytest

def pytest_addoption(parser):
    parser.addoption('--slow', action='store_true', default=False,
                      help='Also run slow tests')

def pytest_runtest_setup(item):
    """Skip tests if they are marked as slow and --slow is not given"""
    if getattr(item.obj, 'slow', None) and not item.config.getvalue('slow'):
        py.test.skip('slow tests not requested')
```

Test the behavior:

```bash
uv run pytest
```

```bash
uv run pytest --slow
```

```bash
uv run pytest --help
```

```bash
uv run pytest --help | grep -B 2 slow
```
