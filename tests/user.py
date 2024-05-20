import asyncio
from bson import ObjectId
from app.Services import User_crud as userFunc
from app.models.user import User
import unittest

class TestHH(unittest.TestCase):
    def test_login(self):
        user = User(id=2, name="bbb", password="bbb")
        result = asyncio.run(userFunc.login(user))
        assert result == {'_id': ObjectId('660d52241a6e46f1e679cad7'), 'id': 2, 'name': 'bbb', 'password': 'bbb'}

    def test_signUp(self):
        user = User(id=11111, name="aaa", password="s@sw.fdfg")
        result = asyncio.run(userFunc.signUp(user))
        assert result == "sighUp"

    def test_updateUser(self):
        user = User(id=11111, name="a", password="s@sw.fdfg")
        result = asyncio.run(userFunc.updateUser(user))
        assert result == "update"
