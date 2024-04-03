import uvicorn as uvicorn
from fastapi import FastAPI
from app.Router.User_Router import user_router
from app.Router.budgetManagment_Router import budgetManagment_Router

app = FastAPI()

app.include_router(user_router, prefix='/user')
app.include_router(budgetManagment_Router, prefix='/budget')

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)

