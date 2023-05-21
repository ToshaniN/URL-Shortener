from flask_restful import Resource, Api,request
from url_shortner_handler import *

class Foo(Resource):

    def post(self):
        data = request.get_json()
        return {"msg": "inside foo post","data": data}


class Bar(Resource):

    def get(self):
        return {"msg": "inside bar get"}
    

class GetShortUrl(Resource):
    def post(self):
        data = request.get_json()
        return UrlHandler().get_short_url(data)