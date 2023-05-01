#!/usr/bin/python3
"""Index file for package views"""

from api.v1.views import app_views
from flask import jsonify

from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.state import State
from models.city import City
from models.review import Review

models={'amenities': Amenity,
       'place': Place,
       'user' : User,
       'state' : User,
       'state' : State,
       'city' : City,
       'review' : review
       }

@app_views.route('/status', methods=['GET'])
def get_status():
    return jsonify(status="OK")

@app_views.route('/stats', methods=['GET'])
def get_count();
stats = {}
for name, model in models.item():
total = storage.count(model)
stats[name] = total
return jsonify(stats)
