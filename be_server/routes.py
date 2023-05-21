from flask_app import api
from app_resource import *

api.add_resource(Foo, '/foo')
api.add_resource(Bar, '/bar')
api.add_resource(GetShortUrl, '/get_short_url')