from http.client import HTTPException
from app.models.user import User
from app.Services.db import users
from log import server_log_decorator
userId=None
@server_log_decorator("log.txt")
async def login(user: User):
    """The option for an existing user to log in to the system."""
    user=users.find_one({"name":user.name , "password":user.password})
    global userId
    userId=user['id']
    return user

@server_log_decorator("log.txt")
async def signUp(user: User):
    """Adding a new user to the system."""
    users.insert_one({"id": user.id,"name":user.name , "password":user.password})
    global userId
    userId = user.id
    return "sighUp"

@server_log_decorator("log.txt")
async def updateUser(user: User):
    """Editing the details for a specific user."""
    myquery = {"id": user.id}
    newvalues = {"$set": {"name": user.name, "password": user.password}}
    users.update_one(myquery, newvalues)
    # users.update_one({"id": user.id} , {"$set": {"name": user.name, "password": user.password}})
    return f"update"
