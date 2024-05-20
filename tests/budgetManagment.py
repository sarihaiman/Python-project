import asyncio
from bson import ObjectId
from app.Services import budgetManagment_crud as budgetFunc
from app.models.budgetManagment import budgetManagment as Budget
import unittest


class TestHH(unittest.TestCase):

    def test_addToBudget(self):
        budget = Budget(userId=11111, expenses=700, revenues=600,id=2,date="17/05/40")
        result = asyncio.run(budgetFunc.addToBudget(budget))
        assert result == "addToBudget"

    def test_updateToBudget(self):
        budget = Budget(userId=11111, expenses=70, revenues=60,id=2,date="17/06/40")
        result = asyncio.run(budgetFunc.updateBudget(budget))
        assert result == "updateBudget"

    def test_deleteBudget(self):
        result = asyncio.run(budgetFunc.deleteBudget(0))
        assert result == "deleteBudget"

if __name__ == '__main__':
    unittest.main()
