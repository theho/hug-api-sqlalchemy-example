import hug
from api import app
from . import APITest


class UsersTest(APITest):
    def test_a(self):
        resp = hug.test.post(app, 'users/signup', {'username': '123', 'password': '123'})
        print(resp)
        self.assertIsNotNone(resp.data['token'],resp.data['token'])

    def test_b(self):

        resp = hug.test.post(app, 'users/signup', {'username': '123', 'password': '123'})
        print(resp)
        self.assertIsNotNone(resp.data['token'], resp.data['token'])

