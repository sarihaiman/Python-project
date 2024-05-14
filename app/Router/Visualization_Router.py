from fastapi import APIRouter,HTTPException
from app.Services import Visualization
from flask import Flask, render_template, request
Visualization_Router = APIRouter()

app = Flask(__name__)
@Visualization_Router.post('/plot')
async def PostVisualization():
    try:
        a = await Visualization.plot()
        print(a)
        return "Visualization"
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error Visualization")
