import hug

from sqlalchemy import create_engine, orm


class SQLAlchemy:
    def __init__(self):
        self.engine = None
        self.session = None
        self._conn_str = None

    def connect(self, **settings):
        sm = orm.sessionmaker(bind=self.engine, autoflush=True, autocommit=True, expire_on_commit=True)
        self.session = orm.scoped_session(sm)

    def close(self):
        self.session.close()

    def init_app(self, app, conn_str):
        self._conn_str = conn_str
        self.engine = create_engine(self._conn_str)

        @hug.request_middleware(api=app)
        def process_data(request, response):
            self.connect()

        @hug.response_middleware(api=app)
        def process_data(request, response, resource):
            self.close()

        return app
