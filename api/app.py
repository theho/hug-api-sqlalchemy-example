import hug

from api.g import db, config
from api.resources import users
from api.ext import auth

app = hug.API(__name__)

# init DB
db.init_app(app, config.SQLALCHEMY_DATABASE_URI)
auth.init_app(app)


# Resources
app.extend(users, '/users')
