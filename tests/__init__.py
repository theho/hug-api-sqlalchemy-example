import os

import unittest
from sqlalchemy_utils import database_exists, create_database, drop_database

from alembic import command
from alembic.config import Config

from api.g import db, config

TESTDB_URI = config.SQLALCHEMY_DATABASE_URI + '_test'
MIGRATIONS = os.path.join(os.getcwd(), '..', 'migrations')


class APITest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 1. Create DB
        if not database_exists(TESTDB_URI):
            create_database(TESTDB_URI)

        # 2. Migrate Tables
        alembic_cfg = Config("../alembic.ini")
        alembic_cfg.set_main_option('script_location', MIGRATIONS)
        alembic_cfg.set_main_option('sqlalchemy.url', TESTDB_URI)

        command.upgrade(alembic_cfg, 'head')

        # replace db with test db connection string
        db._conn_str = TESTDB_URI

    @classmethod
    def tearDownClass(cls):
        drop_database(TESTDB_URI)

    def setUp(self):
        db.connect()

    def tearDown(self):
        db.close()
