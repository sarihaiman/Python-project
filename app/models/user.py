from pydantic import BaseModel


class User(BaseModel):
    name: str
    id: int
    password:str
