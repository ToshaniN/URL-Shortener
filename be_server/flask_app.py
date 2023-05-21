from flask import Flask, session
from flask_cors import CORS, cross_origin
from flask_restful import Api

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from orm import _dbengine


flask_app = Flask(__name__)
api = Api(flask_app)

CORS(flask_app, max_age=1000, supports_credentials = True)
import time

Session = sessionmaker(bind=_dbengine)
dbsession = scoped_session(Session)