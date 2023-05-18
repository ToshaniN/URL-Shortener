from handler import Handler
from flask_restful import Resource
from flask import request, make_response

# '/'
class Home(Resource):
    def get(self):
        return make_response(Handler.home()) 

# '/WantShortURL/'
class WantShortURL(Resource):
    def get(self):
        longURL = request.args.get('longURL')
        return Handler.getShortURL(longURL)

# '/WantLongURL/'
class WantLongURL(Resource):
    def post(self):
        receivedShortURL = request.get_json()
        shortURL = receivedShortURL["shortURL"]
        return Handler.getLongURL(shortURL)
