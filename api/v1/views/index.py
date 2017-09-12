#!/usr/bin/python3
"""
    index.py file in v1/views
"""
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage
app = Flask(__name__)


@app_views.route("/status")
def status_message():
    """method to return an OK status"""
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def count_classes():
    """
        Method to return a jsonified dictionary of stats.
    """
    # Get the count of each Class
    amenities_count = storage.count('Amenity')
    cities_count = storage.count('City')
    places_count = storage.count('Place')
    reviews_count = storage.count('Review')
    states_count = storage.count('State')
    users_count = storage.count('User')
    # Create dictionary
    stat_dict = {}
    # Add to the dictionary
    stat_dict["amenities"] = amenities_count
    stat_dict["cities"] = cities_count
    stat_dict["places"] = places_count
    stat_dict["reviews"] = reviews_count
    stat_dict["states"] = states_count
    stat_dict["users"] = users_count
    # jsonify and return dictionary
    return jsonify(stat_dict)
