from fastapi import APIRouter,HTTPException
from app.Services import Visualization

Visualization_Router = APIRouter()
@Visualization_Router.get('')
async def getVisualization():
    try:
        a = await Visualization.visualization()
        print(a)
        return "Visualization"
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error Visualization")
