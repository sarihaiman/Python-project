from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import requests

app = Flask(__name__)

@app.route('/plot', methods=['POST'])
def plot():
    response = requests.get('http://127.0.0.1:8000/budget?userId=0')
    if response.status_code == 200:
        data = response.json()  # המרת התגובה ל JSON
        plt.plot(data['revenues'], data['expenses'], marker='o', linestyle='-')
        # יצירת ויזואליזציה מתאימה (לדוגמה, גרף)
        # הגדרת כותרת וכווץ
        plt.title('Visualization of Data')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        # הצגת הוויזואליזציה
        plt.show()
    plt.savefig('static/plot.png')
    return render_template('plot.html')


if __name__ == '__main__':
    app.run(debug=True)
