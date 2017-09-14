#!/usr/bin/python3
"""
    places_amenity.py file in v1/views
"""
from flask import abort, Flask, jsonify, request
from api.v1.views import app_views
from models import storage
from models.base_model import BaseModel
from models.place import Place, PlaceAmenity
from models.amenity import Amenity

to_json = BaseModel.to_json


@app_views.route("/places/<string:place_id>/amenities", methods=['GET'])
def get_all_amenity_of_place(place_id):
    """
        Method to return a JSON representation of all amenities based place
    """
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    amenity_list = []
    for amenity in place.amenities:
        amenity_list.append(amenity.to_json())
    return jsonify(amenity_list)


@app_views.route(
    "/places/<string:place_id>/amenities/<string:amenity_id>",
    methods=['DELETE'])
def get_a_place_amenity(place_id, amenity_id):
    """
        Method to return a JSON representation of a amenity based on place
    """
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    amenity = storage.get("Amenity", amenity_id)
    if amenity is None:
        abort(404)
    if amenity not in place.amenities:
        abort(404)
    else:
        storage.delete(amenity)
        response = jsonify({})
        return response, 200


@app_views.route(
    "/places/<string:place_id>/amenities/<string:amenity_id>",
    methods=['POST'])
def create_a_amenity_to_place(place_id, amenity_id):
    """
        Method to create an amenity linked to place
    """
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    amenity = storage.get("Amenity", amenity_id)
    if amenity is None:
        abort(404)
    if amenity in place.amenities:
        return jsonify(amenity.to_json()), 200
    else:
        return jsonify(amenity.to_json()), 201
