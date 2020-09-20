# Imports
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
# Custom Libraries
from data.modelbase import SqlAlchemyBase

__factory = None


def global_init():
    global __factory

    if __factory:
        return

    # TODO: (To the end user) - Make sure to update this to YOUR database
    conn_str = 'postgresql+psycopg2://postgres:postgres@localhost:5432/example_db'
    engine = sa.create_engine(conn_str, echo=False)

    __factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    import data.__all_models

    # Create Tables from the Models
    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory

    session: Session = __factory()
    session.expire_on_commit = False

    return __factory()
