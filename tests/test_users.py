import hug
from api import app
from . import APITest


class UsersTest(APITest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        resp = hug.test.post(app, 'users/signup', headers={'Authorization': 'Bearer XXX'},
                             body={'username': '123', 'password': '444'})

    def test_a(self):
        # resp = hug.test.post(app, 'users/signup', headers={'Authorization': 'Bearer XXX'},
        #                      body={'username': '123', 'password': '444'})
        # print(resp.data['token'])
        # self.assertIsNotNone(resp.data['token'], resp.data['token'])
        resp = hug.test.post(app, 'users/token', body={'username': '123', 'password': '444'})
        # print(resp.data['token'])
        print(resp.status)
