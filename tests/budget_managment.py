import asyncio
from bson import ObjectId
from app.service import budget_managment_crud as budget_func
from app.models.budget_management_model import budget_management as Budget
import unittest


class TestHH(unittest.TestCase):

    def test_add_to_budget(self):
        budget = Budget(userId=888, expenses=700, revenues=600, id=2, date="17/05/40")
        result = asyncio.run(budget_func.add_to_budget(budget))
        assert result == "add_to_budget"

    def test_update_to_budget(self):
        budget = Budget(userId=11111, expenses=70, revenues=60, id=2, date="17/06/40")
        result = asyncio.run(budget_func.update_budget(budget))
        assert result == "update_budget"

    def test_delete_budget(self):
        result = asyncio.run(budget_func.delete_budget(0))
        assert result == "delete_budget"


if __name__ == '__main__':
    unittest.main()
