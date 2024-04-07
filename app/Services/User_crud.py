from http.client import HTTPException
from app.models.user import User
from app.Services.db import users

async def login(user: User):
    user=users.find_one({"name":user.name , "password":user.password})
    print("!!!!!!!!!!!!!!!!!!!!!!!!")
    return user

async def signUp(user: User):
    users.insert_one({"id": user.id,"name":user.name , "password":user.password})
    return f"sighUp"

async def updateUser(user: User):
    myquery = {"id": user.id}
    newvalues = {"$set": {"name": user.name, "password": user.password}}
    users.update_one(myquery, newvalues)
    # users.update_one({"id": user.id} , {"$set": {"name": user.name, "password": user.password}})
    return f"update"