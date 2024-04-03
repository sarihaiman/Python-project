from http.client import HTTPException
from app.models.budgetManagment import budgetManagment as budget
from app.Services.db import budgetManagment

async def addToBudget(budgetManagment: budget):
    print(budgetManagment)
    a={"expenses":1 , "revenues":1,"userId": 1}
    print(a)
    budgetManagment.insert_one(a)
    return "addToBudget"

async def updateBudget(budgetManagment: budget):
    myquery = {"userId": budgetManagment.userId}
    newvalues = {"$set": {"expenses": budgetManagment.expenses, "revenues": budgetManagment.revenues}}
    budgetManagment.update_one(myquery, newvalues)
    return "updateBudget"

async def getBudget(UserId):
    for user in budgetManagment.find({"userId" :int(UserId)}):
        return user

async def deleteBudget(userId):
    budgetManagment.delete_one({"userId":int(userId)})
    return "deleteBudget"

# async def get_all_users():
#     budgetManagment.find()
#     # return [budget(**user) for user in budgetManagment.find()]
#     for user in budgetManagment.find():
#         print(user)

