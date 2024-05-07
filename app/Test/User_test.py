from bson import ObjectId

from app.Services import User_crud as a
from app.models.user import User

import unittest
import asyncio
class TestHH(unittest.TestCase):
    def test_login(self):
        user = User(id=0, name="string", password="string")
        result = asyncio.run(a.login(user))
        assert result == {'_id': ObjectId('663a626ed6b86d4d57cda22c'),'id':0, 'name':"string", 'password':"string"}

    def test_signUp(self):
        user = User(id=112, name="string", password="string")
        result = asyncio.run(a.signUp(user))
        assert result == "sighUp"

    def test_UpdateBudget(self):
        user = User(id=48, name="aaa", password="gfhfgkjgkhjk")
        result = asyncio.run(a.updateUser(user))
        assert result == "update"

if __name__ == '__main__':
    unittest.main()
