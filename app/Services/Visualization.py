from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import requests

app = Flask(__name__)
async def plot():
    # response = requests.get('http://127.0.0.1:8000/budget?userid=0')
    # print(response)
    # if response.status_code == 200:
    #     data = response.json()
        # plt.plot(data['revenues'], data['expenses'], marker='o', linestyle='-')
        plt.plot(45, 23, marker='o', linestyle='-')
        plt.title('Visualization of Data')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.show()
    # # plt.savefig('static/plot.jpg')
    # # return render_template('plot.html')
        return "good"

