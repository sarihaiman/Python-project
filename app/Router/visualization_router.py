from fastapi import APIRouter, HTTPException
from app.service import visualization_crud
from flask import Flask, render_template, request

visualization_router = APIRouter()


@visualization_router.post('/plot')
async def post_visualization():
    """Display data segmentation for the user regarding income and expenses."""
    try:
        await visualization_crud.plot()
        return "visualization"
    except Exception:
        raise HTTPException(status_code=400, detail="oops... an error visualization")

