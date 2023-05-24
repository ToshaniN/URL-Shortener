from handler import Handler
from flask_restful import Resource
from flask import request, make_response
from flask_cors import cross_origin

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
    # def options(self):
    #     response = make_response()
    #     response.headers.add("Access-Control-Allow-Origin", "*")
    #     response.headers.add('Access-Control-Allow-Headers', "*")
    #     response.headers.add('Access-Control-Allow-Methods', "*")
    #     response.headers.add('Content-Type', 'application/json')
    #     return response
    
    def post(self):
        receivedShortURL = request.get_json()
        shortURL = receivedShortURL["shortURL"]
        return Handler.getLongURL(shortURL)
