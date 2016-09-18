import hug
from api.g import db
from api.models.users import User
from sqlalchemy.sql import exists
from falcon.http_error import HTTPError
from falcon.http_status import HTTPStatus

@hug.get('/')
def root():
    # print(list(db.session.execute('select * from profile')))
    return "Users"


@hug.post('/token')
def login(username, password):
    print(db.session.query(User).all())
    return {'token': username + password}


@hug.post('/signup')
def signup(username, password):
    if db.session.query(exists().where(User.username == username)).scalar():
        raise HTTPError(404, title='Cannot', description='asdfas')

    u = User(username=username, password=password)
    print(u)
    db.session.add(u)
    # db.session.commit()
    # print(db.session.query(User).all())

    return {'token': username + password}


if __name__ == '__main__':
    from api import app

    db.connect()
    print(signup('asd2', 'asd'))
