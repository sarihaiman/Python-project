import matplotlib.pyplot as plt
from app.service import budget_managment_crud


async def plot():
    """Retrieve the user's UserID and display for them data segmentation regarding income and expenses."""
    arr = await budget_managment_crud.get_budget()
    x = []
    y = []
    for i in arr:
        x.append(i['revenues'])
        y.append(i['expenses'])
    print(x)
    print(y)
    plt.plot(x, y)
    plt.title('Visualization of Data')
    plt.xlabel('revenues')
    plt.ylabel('expenses')
    plt.show()
    return "good"
