from flask_app import *

class UrlHandler():
    
    def __init__(self):
        self.dbsession = dbsession
    
    def get_short_url(self, data):
        print(data)
        # db session filter query to fetch shorturl
        return data