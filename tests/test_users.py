import os

import hug

from api.resources import users
from . import APITest


class UsersTest(APITest):
    def test_a(self):
        resp = hug.test.post(users, 'signup', {'username': '123', 'password': '123'})
        self.assertIsNotNone(resp.data['token'])
