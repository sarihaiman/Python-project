from bson import ObjectId
from app.Services import budgetManagment_crud as a
from app.models.budgetManagment import budgetManagment

import unittest
import asyncio
class TestHH(unittest.TestCase):
    def test_addToBudget(self):
        budget = budgetManagment(userId=542, expenses=700, revenues=600)
        result = asyncio.run(a.addToBudget(budget))
        assert result == "addToBudget"

    def test_getBudget(self):
        result = asyncio.run(a.getBudget(4))
        assert result == {'_id': ObjectId('66388a6ad500a9e172a3896c'), 'expenses': 1, 'revenues': 0, 'userId': 4}

    def test_UpdateBudget(self):
        budget = budgetManagment(userId=6, expenses=40, revenues=60)
        result = asyncio.run(a.updateBudget(budget))
        assert result == "updateBudget"

    def test_DeleteBudget(self):
        result = asyncio.run(a.deleteBudget(4))
        assert result =="deleteBudget"

if __name__ == '__main__':
    unittest.main()











