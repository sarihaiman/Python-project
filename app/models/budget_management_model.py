from pydantic import BaseModel


class budget_management(BaseModel):
    id: int
    date: str
    expenses: int
    revenues: int
    userId: int
