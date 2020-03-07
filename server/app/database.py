from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class FastDB(object):

    def __init__(self):
        self.engine = None
        self.Session = None
        self.Model = declarative_base()

    def init_db(self, database_url):
        self.engine = create_engine(database_url)
        self.Session = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

    def get_db(self):
        try:
            session = self.Session()
            yield session
        finally:
            session.close()

    def drop_all(self):
        self.Model.metadata.drop_all(self.engine)

    def create_all(self):
        self.Model.metadata.create_all(self.engine)
