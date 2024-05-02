import pytest
from app.Router.budgetManagment_Router import budgetManagment_Router
from app.Services import budgetManagment_crud as a
from app.models.budgetManagment import budgetManagment as budget

# @pytest.mark.int
# def test_add():
# assert a.addToBudget({"userId": 1,"expenses": 23 , "revenuesssss": 65})=="addToBudget"

def test_add():
    print(add(2,3))
    assert add(2,3) == 5

def add(c,x):
    return c+x