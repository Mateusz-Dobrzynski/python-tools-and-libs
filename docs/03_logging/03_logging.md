# 3. Providing observability with logging 📝

## Creating a logger

1. Create a file-specific logger:

```py
import logging
logger = logging.getLogger(__name__)
```

2. Add `pyyaml` to handle a logging conf file:
```bash
uv add pyyaml
```

3. Place [`logging_conf.yaml`](./logging_conf.yaml) in the root of your project.

Run uvicorn with configured logging:
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

## Configuring logging in the source code

### Standalone logging (no configuration file needed)

```py
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s",
    force=True,
)

logger = logging.getLogger(__name__)

logger.info("Hello World!")
```

### With `logging-conf.yaml`


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
