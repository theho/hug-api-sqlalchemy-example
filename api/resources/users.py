import hug
from api.g import db
from api.models.users import User


@hug.get('/')
def root():
    # print(list(db.session.execute('select * from profile')))
    return "Users"


@hug.post('/token')
def login(username, password):
    print(db.session.query(User).all())
    return {'token': username + password}


@hug.local()
@hug.post('/signup')
def signup(username, password):
    print(db.session.query(User).all())
    return {'token': username + password, 'users': db.session.query(User).all()}


if __name__ == '__main__':
    from api import app

    db.connect()
    print(signup('asd', 'asd'))
