from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
from app.service import user_crud
from app.models.user_model import user

user_router = APIRouter()


@user_router.post('/login')
async def login(user: user):
    """Routing that allows an existing user to log in to the system."""
    thisUser: user
    try:
        this_user = await user_crud.login(user)
        if this_user is None:
            raise ValidationError
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error login")
    return f"log-in {this_user['name']}"


@user_router.post('/signUp')
async def sign_up(user: user):
    """Routing that allows a new user to register for the system."""
    try:
        await user_crud.sign_up(user)
        return "sign_up"
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error sign_up")


@user_router.put('')
async def update_user(user: user):
    """Routing that enables editing details of a specific user."""
    try:
        await user_crud.update_user(user)
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error put_user")
    return f"update"
