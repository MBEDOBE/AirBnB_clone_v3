#!/usr/bin/python3
"""The api's application module"""

import os
from flask import Flask
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')
CORS(app, origins=["0.0.0.0"])

@app.errorhandler(404)
def not_found(exception):
    """Takes care of 404 errors"""
    return make_response(jsonify({'error': 'NOT FOUND'}), 404)

@app.teardown_appcontext
def close_storage(exception):
    """Method to handle teardown context"""
    storage.close()


if __name__ == '__main__':
    host = os.getenv('HBNB_API_HOST') or '0.0.0.0'
    port = os.getenv('HBNB_API_PORT') or 5000
    app.run(host=host, port=port, threaded=True, debug=True)
