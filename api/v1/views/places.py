#!/usr/bin/python3
"""
    places.py file in api/v1/views
"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage
from models.base_model import BaseModel
from models.place import Place

to_json = BaseModel.to_json


@app_views.route('/cities/<string:city_id>/places', methods=['GET'])
def get_all_places(city_id):
    """
        Method to rerieve a list of all Place objects of a City
    """
    # Retrieve the City object
    city = storage.get("City", city_id)
    # If City doesn't exist, raise a 404 error
    if city is None:
        abort(404)
    # Create a list to hold all places
    places_list = []
    # Get places from CIty object, add to places_list
    for place in city.places:
        places_list.append(place.to_json())
    return (jsonify(places_list))


@app_views.route('/places/<string:place_id>', methods=['GET'])
def get_a_place(place_id):
    """
        Method to retrieve a Place object
    """
    # Retrive the Place object
    one_place = storage.get("Place", place_id)
    # if Place doesn't exist, raise a 404 error
    if one_place is None:
        abort(404)
    # Return the object
    return (jsonify(one_place.to_json()))


@app_views.route('/places/<string:place_id>', methods=['DELETE'])
def delete_a_place(place_id):
    """
        Method to delete a Place object
    """
    # if Place doesn't exist, raise a 404 error
    # Return empty dictionary with status code 200
    pass


@app_views.route('/cities/<string:city_id>/places', methods=['POST'])
def post_a_place(city_id):
    """
        Method to create a Place object
    """

    # if City object doesn't exist, raise a 404 error
    if not storage.get("City", city_id):
        abort(404)
    # Transform HTTP request to a dictionary
    json_data = request.get_json()
    # if HTTP request is not valid JSON, raise a 400 error
    if not json_data:
        return jsonify({"message": "Not a JSON"}), 400
    # if request doesn't contain key 'user_id', raise a 400 error
    user_id = json_data.get("user_id")
    if not user_id:
        return jsonify({"message": "Missing user_id"}), 400
    # if User doesn't exist, raise a 404 error
    if not storage.get("User", user_id):
        abort(404)
    # if request doesn't contain key 'name', raise a 400 error
    if not json_data.get("name"):
        return jsonify({"message": "Missing name"}), 400
    # Create a new_place_dict to hold all info for Place object
    new_place_dict = {}
    # Update new_place_dict with dictionary from request
    new_place_dict.update(json_data)
    # Add city_id to the dictionary
    new_place_dict["city_id"] = city_id
    # Create and save new Place object
    new_place = Place(**new_place_dict)
    new_place.save()
    # to_json() the Place object
    json_place = new_place.to_json()
    # Return new Place with status code 201
    return jsonify(json_place), 201


@app_views.route('/places/<string:place_id>', methods=['PUT'])
def put_a_place(place_id):
    """
        Method to update a Place object
    """
    # if Place object doesn't exist, raise a 404 error
    # use request.get_json() to transform HTTP request to a dictionary
    # if HTTP request body is not valid JSON, raise a 400 error with message "Not a JSON"
    # Create dictionary of keys to not update
    # Update Place object, ignoring the keys in ignore_keys
    # Return Place object with status code 200
    pass
