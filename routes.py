from __main__ import app
from resources import Resource

class Routes:
    app.add_url_rule('/', view_func=Resource.home)
    app.add_url_rule('/WantShortURL/', view_func=Resource.get)    
    app.add_url_rule("/WantLongURL/", view_func=Resource.post, methods=['POST'])

