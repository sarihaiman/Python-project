from http.client import HTTPException
from app.models.user_model import user
from app.service.db import users
from app.log import server_log_decorator

userId = None


@server_log_decorator("log.txt")
async def login(user_one: user):
    """The option for an existing user to log in to the system."""
    user_now = users.find_one({"name": user_one.name, "password": user_one.password})
    print(user_now)
    global userId
    userId = user_now['id']
    return user_now


@server_log_decorator("log.txt")
async def sign_up(user_one: user):
    """Adding a new user to the system."""
    user_now = users.find_one({"id": user_one.id})
    if user_now is None:
        users.insert_one({"id": user_one.id, "name": user_one.name, "password": user_one.password})
        global userId
        userId = user_one.id
        return "sigh_up"
    else:
        raise HTTPException(status_code=400, detail="id error - id exist")


@server_log_decorator("log.txt")
async def update_user(user_one: user):
    """Editing the details for a specific user."""
    myquery = {"id": userId}
    new_values = {"$set": {"name": user_one.name, "password": user_one.password}}
    users.update_one(myquery, new_values)
    return f"update"
