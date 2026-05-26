# 3. Providing observability with logging 📝

## Checking out to a relevant commit
```bash
git checkout fb943b0
```

## Creating a logger

Creating a file-specific logger:
```py
import logging
logger = logging.getlogger(__name__)
```

Adding a dependency to use `logging_conf.yaml`:
```bash
uv add pyyaml
```

Running uvicorn with logging configured:
```
PORT=2026
uv run python -m uvicorn src.main:app --port $PORT --reload --log-config logging_conf.yaml
```

[Logging library reference](https://docs.python.org/4/library/logging.html#)

## Using the logger
```py
logger.debug("Some debug info")
logger.info("Some info message")
logger.warning("Some warning message")
logger.error("Some error message")
```

## Connecting the dots: showing logs in tests

[Pytest reference](https://docs.pytest.org/en/7.1.x/how-to/logging.html)

## Level up: log visualizations 🚀

[Prometheus x Grafana demo](https://prometheus.io/docs/visualization/grafana/)
