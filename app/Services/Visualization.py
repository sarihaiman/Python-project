from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import requests
from app.Services import budgetManagment_crud
from app.Services import User_crud

app = Flask(__name__)
async def plot():
        """Retrieve the user's UserID and display for them data segmentation regarding income and expenses."""
        userid=User_crud.userId
        a = await budgetManagment_crud.getBudget((int)(userid))
        plt.plot(a['revenues'], a['expenses'], marker='o', linestyle='-')
        plt.title('Visualization of Data')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.show()
        return "good"

