# Debugging with uv with VS Code

## Checking out to a relevant commit
```bash
git checkout 7320625
```

## Setting up a debugger

1. Install VS Code extensions

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) (ms-python.python)
- [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy) (ms-python.debugpy)

**Hint:** these extensions can be installed by pressing `Ctrl+P` and pasting the following (one by one):

- `ext install ms-python.python`
- `ext install ms-python.debugpy`

2. Paste the following into `.vscode/launch.json`

```json
{
  "version": "0.2.0",
  "configurations": [
    {
        "name": "uv debug (basic)",
        "type": "debugpy",
        "request": "launch",
        "python": ".venv/bin/python",
        "module": "uvicorn",
        "args": ["src.main:app"]
    }
  ]
}
```

3. Enter a file you want to debug and start a debugging session.

<img src="https://code.visualstudio.com/assets/docs/debugtest/debugging/debug-start.png">

>[Debug code with Visual Studio Code](https://code.visualstudio.com/docs/debugtest/debugging#_start-a-debugging-session)

**TO-DO:** modify the config to:
- Enable logging,
- Reload the file ,
- Define a custom port to expose.

## Debugging pytest runs

```json
{
  "name": "Pytest: Debug",
  "type": "debugpy",
  "request": "launch",
  "python": ".venv/bin/python",
  "module": "pytest",
  "console": "integratedTerminal",
  "justMyCode": true,
  "env": {
    "PYTHONPATH": "${workspaceFolder}"
  }
}
```

## Debugging in action
Test `test_loyal_users.py` and examine the source of failures.
