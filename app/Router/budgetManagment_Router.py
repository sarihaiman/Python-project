from http.client import HTTPException
from fastapi import APIRouter
from pydantic import ValidationError
from app.Services import budgetManagment_crud
from app.models.budgetManagment import budgetManagment as budget

budgetManagment_Router = APIRouter()

@budgetManagment_Router.get('')
async def getBudget(userid):
     a = await budgetManagment_crud.getBudget(userid)
     return {  "expenses": a['expenses'] , "revenues" : a['revenuesssss'], "userId": a['userId']}

@budgetManagment_Router.post('')
async def addToBudget(budgetManagment: budget):
    # try:
    await budgetManagment_crud.addToBudget(budgetManagment)
    # except Exception:
    #     raise HTTPException(status_code=400, detail="oops... an error addToBudget")
    return "addToBudget"

@budgetManagment_Router.put('')
async def updateBudget(budgetManagment: budget):
    # try:
    print(budgetManagment)
    await budgetManagment_crud.updateBudget(budgetManagment)
    # except:
    #     raise HTTPException(status_code=400, detail="oops... an error updateBudget")
    return f"updateBudget"

@budgetManagment_Router.delete('')
async def deleteBudget(userid):
    try:
        await budgetManagment_crud.deleteBudget(userid)
    except:
        raise HTTPException(status_code=400, detail="oops... an error deleteBudget")
    return f"deleteBudget"

# @budgetManagment_Router.get('/all')
# async def get_all_users():
#     return await budgetManagment_crud.get_all_users()
