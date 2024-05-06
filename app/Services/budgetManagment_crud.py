from http.client import HTTPException
from app.models.budgetManagment import budgetManagment as budget
from app.Services.db import Managment
from log import server_log_decorator

@server_log_decorator("log.txt")
async def addToBudget(budgetManagment: budget):
    """Adding expenses and revenues of a specific user to the management system."""
    c=Managment.find_one({"userId" : budgetManagment.userId})
    if(c==None):
        Managment.insert_one({"userId": budgetManagment.userId,"expenses": budgetManagment.expenses , "revenues": budgetManagment.revenues})
        return "addToBudget"
    else:
        raise "userId found"

@server_log_decorator("log.txt")
async def updateBudget(budgetManagment: budget):
    """Managing expenses and revenues for a specific user."""
    c = Managment.find_one({"userId": budgetManagment.userId})
    if (c != None):
        myquery = {"userId": budgetManagment.userId}
        newvalues = {"$set": {"expenses": budgetManagment.expenses, "revenues": budgetManagment.revenues}}
        Managment.update_one(myquery, newvalues)
    else:
        raise "userId found"

@server_log_decorator("log.txt")
async def getBudget(UserId):
    """Receiving a report of expenses and revenues for a specific user."""
    try:
        for user in Managment.find({"userId" :int(UserId)}):
            return user
    except:
        raise "userid not found"


@server_log_decorator("log.txt")
async def deleteBudget(userId):
    """Deleting expenses and revenues for a specific user."""
    try:
        Managment.delete_one({"userId":int(userId)})
        return "deleteBudget"
    except:
        raise "userid not found"





