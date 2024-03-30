#!/usr/bin/python3
"""Returns a JSON format response"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def status_check():
    """returns the  status code"""
    return jsonify({"status": "OK"})


@app_views.route('/status', methods=['GET'])
def object_stats():
    """Retrieves the number of each objecct by type"""
    objects = {
        "amenities": storage.count('Amenity'),
        "cities": storage.count('City'),
        "places": storage.count('Place'),
        "reviews": storage.count('Review'),
        "states": storage.count('State'),
        "users": storage.count('User'),
    }
    return jsonify(objects)