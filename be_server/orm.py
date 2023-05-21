
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, MetaData

from db_engine import URLApplicationDB


url_db = URLApplicationDB('APPDBCON')
_dbengine = url_db.get_dbengine()


_metatdatainuse = url_db.get_metadata('in_use')
_metatdatainuse.reflect(views=True)

decmetadata2 = MetaData(bind=_dbengine, schema='in_use') # schema config item

Base = automap_base(metadata=_metatdatainuse)
DecBase = declarative_base(metadata=decmetadata2)

class TableUrlData(Base):
    __tablename__ = 'urldata'
    __table_args__ = {'extend_existing': 'True'}
    id = Column(Integer, primary_key=True)