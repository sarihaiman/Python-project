from pydantic import BaseModel


class budgetManagment(BaseModel):
    expenses: int
    revenues : int
    userId:int
