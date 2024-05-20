from http.client import HTTPException
from app.models.budgetManagment import budgetManagment as budget
from app.Services.db import Managment
from log import server_log_decorator
from app.Services import User_crud
import numpy

@server_log_decorator("log.txt")
async def addToBudget(budgetManagment: budget):
    """Adding expenses and revenues of a specific user to the management system."""
    userid = User_crud.userId
    global count
    try:
        Managment.insert_one({"userId": userid,"expenses": budgetManagment.expenses , "revenues": budgetManagment.revenues,"id": budgetManagment.id,"date": budgetManagment.date})
        return "addToBudget"
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error addToBudget")

@server_log_decorator("log.txt")
async def updateBudget(budgetManagment: budget):
    """Managing expenses and revenues for a specific user."""
    try:
        myquery = {"id": budgetManagment.id}
        newvalues = {"$set": {"expenses": budgetManagment.expenses, "revenues": budgetManagment.revenues,"id": budgetManagment.id,"date": budgetManagment.date}}
        Managment.update_one(myquery, newvalues)
        return "updateBudget"
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error updateBudget")

@server_log_decorator("log.txt")
async def getBudget():
    """Receiving a report of expenses and revenues for a specific user."""
    my_array = []
    userid = User_crud.userId
    try:
        for user in Managment.find({"userId" :(int)(userid)}):
            my_array.append(user)
        return my_array
    except:
        raise "userid not found"


@server_log_decorator("log.txt")
async def deleteBudget(Id):
    """Deleting expenses and revenues for a specific user."""
    try:
        Managment.delete_one({"id":int(Id)})
        return "deleteBudget"
    except:
        raise "userid not found"





