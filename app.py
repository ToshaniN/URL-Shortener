from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

import routes
import database

if __name__ == "__main__":
    app.run(debug=True)
