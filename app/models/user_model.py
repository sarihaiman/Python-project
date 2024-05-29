from pydantic import BaseModel


class user(BaseModel):
    name: str
    id: int
    password: str
