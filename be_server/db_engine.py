from sqlalchemy import create_engine, MetaData, inspect
from sqlalchemy.orm.session import sessionmaker
from project_config import project_config


class URLApplicationDB:

    def __init__(self, appname):
        self._dbconfig =  project_config.get('db_config')
        con_string = "postgresql+psycopg2://{0}:{1}@{2}/{3}".format(self._dbconfig['username'], self._dbconfig['pwd'],
                                                                    self._dbconfig['host'], self._dbconfig['dbname'])
        self._dbengine = create_engine(con_string, echo=False)
        self._metadata = {}

    def get_dbengine(self):
        return self._dbengine

    def get_metadata(self, schemaname):
        return MetaData(bind=self._dbengine, schema=schemaname)

    def get_session(self):
        Session = sessionmaker(bind=self._dbengine)
        return Session()

if __name__ == "__main__":
    pass
