import os

from api.ext.db import SQLAlchemy
from . import settings

ENV_MAPPING = {
    'DEV': settings.DevConfig,
}

db = SQLAlchemy()
config = ENV_MAPPING[os.environ.get('API_ENV', 'DEV')]
