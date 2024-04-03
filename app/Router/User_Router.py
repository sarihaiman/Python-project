from http.client import HTTPException
from fastapi import APIRouter
from pydantic import ValidationError
from app.Services import User_crud
from app.models.user import User

user_router = APIRouter()

@user_router.post('/login')
async def login(user: User):
    thisUser:User
    try:
          thisUser=await User_crud.login(user)
          if thisUser==None:
              raise ValidationError
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error login")
    return f"log-in {thisUser['name']}"

@user_router.post('/signUp')
async def signUp(user: User):
    try:
        await User_crud.signUp(user)
    except:
        raise HTTPException(status_code=400, detail="oops... an error signUp")
    return "signUp"

@user_router.put('')
async def updateUser(user: User):
    try:
        await User_crud.updateUser(user)
    except:
        raise HTTPException(status_code=400, detail="oops... an error putUser")
    return f"update"


