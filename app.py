from flask import Flask

app = Flask(__name__)

import routes
import database

if __name__ == "__main__":
    app.run(debug=True)
