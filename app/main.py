import uvicorn as uvicorn
from fastapi import FastAPI
from app.router.user_router import user_router
from app.router.budget_managment_router import budget_managment_router
from app.router.visualization_router import visualization_router

app = FastAPI()

app.include_router(user_router, prefix='/user')
app.include_router(budget_managment_router, prefix='/budget')
app.include_router(visualization_router, prefix='/visualization')

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)

