import logging

from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

logger = logging.getLogger(__name__)

app = FastAPI()
logger.info("bajojajo")


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
    logger.info("bajojajo")
    try:
        user = User().create(new.username, new.password)
        return user
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")
