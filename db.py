from flask import g
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

IS_POSTGRESQL = False


def init_db(g):
    if IS_POSTGRESQL:
        host = 'mobzoom-server.database.windows.net'
        port = 1433
        dbname = 'mobzoom-database'
        user = 'mobzoom-server-admin'
        password = 'postgres'
        url = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'
    else:
        url = 'sqlite:///python_web.db'
    engine = create_engine(url)
    g.db = sessionmaker(bind=engine)


@contextmanager
def get_db_session():
    if 'db' not in g:
        init_db(g)

    with g.db() as session:
        yield session


def close_db():
    g.pop('db', None)


def init_app(app):
    get_db_session()

