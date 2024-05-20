
from pydantic import BaseModel


class budgetManagment(BaseModel):
    id:int
    date:str
    expenses: int
    revenues : int
    userId:int
