import hug

from api.g import db, config
from api.resources import users

app = hug.API(__name__)

# init DB
db.init_app(app, config.SQLALCHEMY_DATABASE_URI)

# Resources
app.extend(users, '/users')
