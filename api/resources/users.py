import hug
from api.g import db
from api import g
from api.models.users import User

@hug.get('/')
def root():
    """Says happy birthday to a user"""
    print(g.config.APP_DIR)
    # print(list(db.session.execute('select * from profile')))
    return "Users"