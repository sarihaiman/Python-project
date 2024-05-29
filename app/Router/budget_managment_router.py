from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
from app.service import budget_managment_crud
from app.models.budget_management_model import budget_management as budget

budget_managment_router = APIRouter()


@budget_managment_router.get('')
async def get_budget():
    """Routing that allows the user to access details about their expenses and revenues."""
    try:
        s = ""
        my_array = await budget_managment_crud.get_budget()
        for i in my_array:
            s += "expenses: "
            s += (str(i['expenses']))
            s += " revenues: "
            s += (str(i['revenues']))
            s += " userId: "
            s += (str(i['userId']))
            s += " id: "
            s += (str(i['id']))
            s += " date: "
            s += (str(i['date']))
            s += ", "
        return s
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error addToBudget")


@budget_managment_router.post('')
async def add_to_budget(budget_management: budget):
    """Routing that enables adding expenses and revenues for a specific user."""
    try:
        await budget_managment_crud.add_to_budget(budget_management)
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error add_to_budget")
    return "add_to_budget"


@budget_managment_router.put('')
async def update_budget(budget_management: budget):
    """Routing that allows editing expenses and revenues for a specific user."""
    try:
        await budget_managment_crud.update_budget(budget_management)
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error update_budget")
    return f"update_budget"


@budget_managment_router.delete('')
async def delete_budget(user_id:int):
    """Routing that enables deleting expenses and revenues for a specific user."""
    try:
        await budget_managment_crud.delete_budget(user_id)
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error delete_budget")
    return f"delete_budget"
