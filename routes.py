from app import api
from url_resource import *

class Routes:
    api.add_resource(Home, '/')
    api.add_resource(WantShortURL, '/WantShortURL/')
    api.add_resource(WantLongURL, '/WantLongURL')
