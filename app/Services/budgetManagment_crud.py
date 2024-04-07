from http.client import HTTPException
from app.models.budgetManagment import budgetManagment as budget
from app.Services.db import Managment

async def addToBudget(budgetManagment: budget):
    Managment.insert_one({"userId": budgetManagment.userId,"expenses": budgetManagment.expenses , "revenuesssss": budgetManagment.revenuesssss})
    return "addToBudget"

async def updateBudget(budgetManagment: budget):
    print(budgetManagment)
    myquery = {"userId": budgetManagment.userId}
    newvalues = {"$set": {"expenses": budgetManagment.expenses, "revenuesssss": budgetManagment.revenuesssss}}
    Managment.update_one(myquery, newvalues)
    return "updateBudget"

async def getBudget(UserId):
    for user in Managment.find({"userId" :int(UserId)}):
        return user

async def deleteBudget(userId):
    Managment.delete_one({"userId":int(userId)})
    return "deleteBudget"

# async def get_all_users():
#     budgetManagment.find()
#     # return [budget(**user) for user in budgetManagment.find()]
#     for user in budgetManagment.find():
#         print(user)

