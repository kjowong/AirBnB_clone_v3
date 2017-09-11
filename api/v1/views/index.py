#!/usr/bin/python3
"""
    index.py file in v1/views
"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage, amenity, city, place, review, state, user
app = Flask(__name__)


@app_views.route("/status")
def status_message():
    """
        method to return an OK status
    """
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def count_classes():
    """
        method to return a jsonified dictionary of stats.
    """
    class_dict = {
        'Amenity': amenity.Amenity,
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'User': user.User
    }
    # Create dictionary
    stat_dict = {}
    # Add to the dictionary
    for key, value in class_dict.items():
        stat_dict[key] = storage.count(key)
    return jsonify(stat_dict)
