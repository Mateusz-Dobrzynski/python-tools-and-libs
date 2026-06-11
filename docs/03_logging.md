# 3. Providing observability with logging 📝

## Checking out to a relevant commit
```bash
git checkout fb943b0
```

## Creating a logger

Creating a file-specific logger:

```py
import logging
logger = logging.getLogger(__name__)
```

Adding a dependency to use `logging_conf.yaml`:
```bash
uv add pyyaml
```

Running uvicorn with logging configured:
```bash
uv run python -m uvicorn src.main:app --reload --log-config logging_conf.yaml
```
- `--log-config logging_conf.yaml`: loads the custom logging configuration from `logging_conf.yaml`.


[Logging library reference](https://docs.python.org/4/library/logging.html#)

## Using the logger
```py
logger.debug("Some debug info")
logger.info("Some info message")
logger.warning("Some warning message")
logger.error("Some error message")
```

## Standalone logging

A minimal example of standalone logging (`logging-conf.yaml` required):

```py
import logging.config
from logging import getLogger

import yaml

with open("logging_conf.yaml", "r", encoding="utf-8") as f:
    logging.config.dictConfig(yaml.safe_load(f))

logger = getLogger(__name__)

logger.info("Hello World!")
```

## Connecting the dots: showing logs in tests

[Pytest reference](https://docs.pytest.org/en/7.1.x/how-to/logging.html)

## Level up: log visualizations 🚀

[Prometheus x Grafana demo](https://prometheus.io/docs/visualization/grafana/)
