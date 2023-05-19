from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from sqlalchemy.ext.automap import automap_base
from connect_db import ConnectDB

Base = automap_base()

class mapped_urls(Base):
    __tablename__ = 'mapped_urls'
    Token = Column('Token', Integer, primary_key=True)
    long_URLs = Column('long_URLs', String(500))
    time = Column('time_created', TIMESTAMP, server_default=func.now())
        
engine = ConnectDB.createEngine()
session = ConnectDB.makeSession(engine)

Base.prepare(autoload_with=engine)
