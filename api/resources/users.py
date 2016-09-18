import hug
from api.g import db, config
from api.models.users import User
from sqlalchemy.sql import exists
from falcon import HTTPNotFound
import jwt
import datetime
from sqlalchemy.orm.exc import NoResultFound


@hug.get('/')
def root():
    return "Users"


def generate_token(u: User):
    return jwt.encode({'username': u.username}, config.SECRET_KEY)


@hug.post('/token')
def login(username, password):
    try:
        u = db.session.query(User).filter(User.username == username).one()
    except NoResultFound:
        raise HTTPNotFound(title='Cannot', description='asdfas')

    return {'token': generate_token(u)}


@hug.post('/signup')
def signup(username, password):
    if db.session.query(exists().where(User.username == username)).scalar():
        raise HTTPNotFound(title='Cannot', description='asdfas')

    u = User(username=username, password=password)
    print(u)
    db.session.add(u)

    return {'token': generate_token(u)}


if __name__ == '__main__':
    from api import app

    db.connect()
    print(signup('asd2', 'asd'))
