from http.client import HTTPException
from app.models.budget_management_model import budget_management as budget
from app.service.db import managment
from app.log import server_log_decorator
from app.service import user_crud


@server_log_decorator("log.txt")
async def add_to_budget(budget_management: budget):
    """Adding expenses and revenues of a specific user to the management system."""
    userid = user_crud.userId
    global count
    try:
        managment.insert_one(
            {"userId": userid, "expenses": budget_management.expenses, "revenues": budget_management.revenues,
             "id": budget_management.id, "date": budget_management.date})
        return "add_to_budget"
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error addToBudget")


@server_log_decorator("log.txt")
async def update_budget(budget_management: budget):
    """Managing expenses and revenues for a specific user."""
    try:
        myquery = {"id": budget_management.id}
        new_values = {"$set": {"expenses": budget_management.expenses, "revenues": budget_management.revenues,
                               "id": budget_management.id, "date": budget_management.date}}
        managment.update_one(myquery, new_values)
        return "update_budget"
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error updateBudget")


@server_log_decorator("log.txt")
async def get_budget():
    """Receiving a report of expenses and revenues for a specific user."""
    my_array = []
    userid = user_crud.userId
    try:
        for user in managment.find({"userId": int(userid)}):
            my_array.append(user)
        return my_array
    except Exception:
        raise "userid not found"


@server_log_decorator("log.txt")
async def delete_budget(id_managment):
    """Deleting expenses and revenues for a specific user."""
    try:
        managment.delete_one({"id": int(id_managment)})
        return "delete_budget"
    except Exception:
        raise "userid not found"
