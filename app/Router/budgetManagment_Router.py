from fastapi import APIRouter,HTTPException
from pydantic import ValidationError
from app.Services import budgetManagment_crud
from app.models.budgetManagment import budgetManagment as budget

budgetManagment_Router = APIRouter()

@budgetManagment_Router.get('')
async def getBudget(userid):
    """Routing that allows the user to access details about their expenses and revenues."""
    try:
        a = await budgetManagment_crud.getBudget(userid)
        return { "expenses": a['expenses'] , "revenues" : a['revenues'], "userId": a['userId']}
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error addToBudget")

@budgetManagment_Router.post('')
async def addToBudget(budgetManagment: budget):
    """Routing that enables adding expenses and revenues for a specific user."""
    try:
        await budgetManagment_crud.addToBudget(budgetManagment)
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error addToBudget")
    return "addToBudget"

@budgetManagment_Router.put('')
async def updateBudget(budgetManagment: budget):
    """Routing that allows editing expenses and revenues for a specific user."""
    try:
        await budgetManagment_crud.updateBudget(budgetManagment)
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error updateBudget")
    return f"updateBudget"

@budgetManagment_Router.delete('')
async def deleteBudget(userid):
    """Routing that enables deleting expenses and revenues for a specific user."""
    try:
        await budgetManagment_crud.deleteBudget(userid)
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error deleteBudget")
    return f"deleteBudget"
