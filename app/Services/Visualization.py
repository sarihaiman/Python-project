from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import requests
from app.Services import budgetManagment_crud
from app.Services import User_crud

app = Flask(__name__)
async def plot():
        """Retrieve the user's UserID and display for them data segmentation regarding income and expenses."""
        arr = await budgetManagment_crud.getBudget()
        x=[]
        y=[]
        for i in arr:
            x.append(i['revenues'])
            y.append(i['expenses'])
        plt.plot(x,y)
        plt.title('Visualization of Data')
        plt.xlabel('revenues')
        plt.ylabel('expenses')
        plt.show()
        return "good"

