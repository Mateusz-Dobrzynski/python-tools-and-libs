# 3. Providing observability with logging 📝

# Creating a logger

Creating a file-specific logger:
```py
import logging
logger = logging.getlogger(__name__)
```

Adding a dependency to use `logging_conf.yaml`:
```
uv add pyyaml
```

Running uvicorn with logging configured:
```
PORT=2026
uv run python -m uvicorn src.main:app --port $PORT --reload --log-config logging_conf.yaml
```

[Logging library reference](https://docs.python.org/4/library/logging.html#)

## Using the logger
```
logger.debug("Some debug info")
logger.info("Some info message")
logger.warning("Some warning message")
logger.error("Some error message")
```
