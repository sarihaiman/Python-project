import uvicorn as uvicorn
from fastapi import FastAPI
from app.Router.User_Router import user_router
from app.Router.budgetManagment_Router import budgetManagment_Router
from app.Router.Visualization_Router import Visualization_Router
# from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(user_router, prefix='/user')
app.include_router(budgetManagment_Router, prefix='/budget')
app.include_router(Visualization_Router, prefix='/Visualization')
# app.mount("/Static", StaticFiles(directory="static"), name="static")

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)

