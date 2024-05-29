import asyncio
from bson import ObjectId
from app.service import user_crud as user_func
from app.models.user_model import user as user_test
import unittest


class TestHH(unittest.TestCase):

    def test_sign_up(self):
        user_now = user_test(id=11111, name="aaa", password="s@sw.fdfg")
        result = asyncio.run(user_func.sign_up(user_now))
        assert result == "sigh_up"

    def test_login(self):
        user_now = user_test(id=2, name="aaa", password="s@sw.fdfg")
        result = asyncio.run(user_func.login(user_now))
        assert result == {'_id': ObjectId('665732b9661933728814a8a4'), 'id': 11111, 'name': 'aaa', 'password': 's@sw.fdfg'}

    def test_update_user(self):
        user_now = user_test(id=11111, name="a", password="s@sw.fdfg")
        result = asyncio.run(user_func.update_user(user_now))
        assert result == "update"
