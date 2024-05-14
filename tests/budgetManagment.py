import asyncio
from bson import ObjectId
from app.Services import budgetManagment_crud as budgetFunc
from app.models.budgetManagment import budgetManagment as Budget
import unittest


class TestHH(unittest.TestCase):
    def test_getBudget(self):
        result = asyncio.run(budgetFunc.getBudget(1))
        assert result == {'_id': ObjectId('660d5c67adb1906e8645e5ad'), 'expenses': 500, 'revenues': 10000, 'userId': 1}

    def test_addToBudget(self):
        budget = Budget(userId=11111, expenses=700, revenues=600)
        result = asyncio.run(budgetFunc.addToBudget(budget))
        assert result == "addToBudget!"

    def test_updateToBudget(self):
        budget = Budget(userId=11111, expenses=70, revenues=60)
        result = asyncio.run(budgetFunc.updateBudget(budget))
        assert result == "updateBudget!"

    def test_deleteBudget(self):
        result = asyncio.run(budgetFunc.deleteBudget(11111))
        assert result == "deleteBudget!"


if __name__ == '__main__':
    unittest.main()
