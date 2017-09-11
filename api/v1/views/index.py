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
    # To prettify later: condense
    # Get the count of each Class

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
# stat_dict["amenities"] = amenities_count
#   stat_dict["cities"] = cities_count
#   stat_dict["places"] = places_count
#   stat_dict["reviews"] = reviews_count
#   stat_dict["states"] = states_count
#   stat_dict["users"] = users_count
    # jsonify and return dictionary
    return jsonify(stat_dict)
