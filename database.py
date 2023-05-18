from __main__ import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, func
from sqlalchemy.ext.automap import automap_base
import config

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + config.connection['username'] + ':' + config.connection['password'] + '@localhost:3306/urls'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Base = automap_base()

class mapped_urls(Base):
    __tablename__ = 'mapped_urls'
    Token = Column('Token', Integer, primary_key=True)
    long_URLs = Column('long_URLs', String(500))
    time = Column('time_created', TIMESTAMP, server_default=func.now())
        

connection_string = "mysql+mysqlconnector://" + config.connection['username'] + ':' + config.connection['password'] + "@localhost:3306/urls"
engine = create_engine(connection_string)

Session = sessionmaker(bind=engine)
session = Session()

Base.prepare(autoload_with=engine)
