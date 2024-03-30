#!/usr/bin/python3
"""Creating a Flask Application"""

import os
from flask import Flask
from models import storage
from api.v1.views import app_views
from flask_cors import CORS


#Creating a flask application instance
app = Flask(__name__)

#Registering the blueprint app_views
app.register_blueprint(app_views)

#Initializing CORS with the app instance
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


#Declaring a method to handle teardown
@app.teardown_appcontext
def teardown(exception):
    """Closes the current SQLAlchemy session"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handles the 404 not found error"""
    return({'error': 'Not found'}), 404


if __name__ == '__main__':
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
    #getenv returns a string and port is an int
    #threaded is set to true so it can serve multiple request at once