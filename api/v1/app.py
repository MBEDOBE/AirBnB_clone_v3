#!/usr/bin/python3
'''
    app for registering blueprint and starting flask
'''
import os
from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
CORS(app, origins="0.0.0.0")
app.register_blueprint(app_views, url_prefix='/api/v1')

@app.teardown_appcontext
def close_storage(exception):
    """Method to handle teardown context"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    '''
    return JSON formatted 404 status code response
    '''
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    host = os.getenv('HBNB_API_HOST') or '0.0.0.0'
    port = os.getenv('HBNB_API_PORT') or 5000
    app.run(host=host, port=port, threaded=True, debug=True)
