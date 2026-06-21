# Managing environmental variables

## `.env` file

`.env` file structure:

```bash
VARIABLE=VALUE
echo $VARIABLE
```

```env
VARIABLE=VALUE
```

```bash
source .env
echo $VARIABLE
```

## Environmental variables in Python

Read variable or break:

```py
import os

VARIABLE = os.environ["VARIABLE"]
```

Try/Except:

```py
import os

try:
    VARIABLE = os.environ["VARIABLE"]
except KeyError:
    raise RuntimeError("VARIABLE is not defined")
```

Default value:

```py
import os

VARIABLE = os.environ.get("VARIABLE", "DEFAULT_VALUE")
```


## Environmental variables in `uv`
```bash
VARIABLE=VALUE uv run main.py
```

```bash
uv run --env-file .env main.py 
```

## Preventing the `.env` file from getting leaked

```bash
grep \\.env .gitignore
```
