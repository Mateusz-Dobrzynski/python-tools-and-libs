# 1. Fast API demo

1. Paste the following into `src/main.py`:

```py
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

app = FastAPI()


class NewUser(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    username: str


class User:
    def create(self, username: str, password: str):
        return {"username": username}


@app.post("/users", response_model=UserResponse)
async def create_user(new: NewUser) -> UserResponse:
    try:
        user = User().create(new.username, new.password)
        return user
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

```

2. Start the server:

```
uv run python -m uvicorn main:app --reload
```
- `uv run` – run the following in an environment managed by uv
- `python -m uvicorn` – start the [uvicorn](https://uvicorn.dev/) server
- `main:app` – (for uvicorn): import `app` from the `main` module
- `--reload` – automatically restart the server when code changes are detected

3. Sending a request:
```bash

curl -X POST "http://localhost:8080/users" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "magda_gessler",
    "password": "kuchennerewolucje123"
  }'
```

4. Access documentation:
http://localhost:2026/docs