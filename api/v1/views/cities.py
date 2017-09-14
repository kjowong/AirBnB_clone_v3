#!/usr/bin/python3
"""
    states.py file in v1/views
"""
from flask import abort, Flask, jsonify, request
from api.v1.views import app_views
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.state import State

to_json = BaseModel.to_json


@app_views.route("/states/<string:state_id>/cities", methods=['GET'])
def get_all_cities(state_id):
    """
        Method to return a JSON representation of all cities
    """
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    cities_list = []
    for city in state.cities:
        cities_list.append(to_json(city))
    return (jsonify(cities_list))


@app_views.route("/cities/<string:city_id>", methods=['GET'])
def get_a_city(city_id):
    """
        Method to return a JSON representation of a city
    """
    one_city = storage.get("City", city_id)
    if one_city is None:
        abort(404)
    return (jsonify(to_json(one_city)))


@app_views.route("/cities/<string:city_id>", methods=['DELETE'])
def delete_a_city(city_id):
    """
        Method to delete a city
    """
    to_delete = storage.get("City", city_id)
    if to_delete is None:
        abort(404)
    else:
        storage.delete(to_delete)
        response = jsonify({})
        return response, 200


@app_views.route("/states/<string:state_id>/cities", methods=['POST'])
def create_a_city(state_id):
    """
        Method to create a city
    """
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    json_data = request.get_json()
    if not json_data:
        return jsonify({"message": "Not a JSON"}), 400
    name = json_data.get("name")
    if name is None:
        return jsonify({"message": "Missing name"}), 400
    new_city_dict = {}
    new_city_dict.update(json_data)
    new_city_dict["state_id"] = state_id
    new_city = City(**new_city_dict)
    new_city.save()
    json_city = new_city.to_json()
    return jsonify(json_city), 201


@app_views.route('/cities/<string:city_id>', methods=['PUT'])
def put_a_city(city_id):
    one_city = storage.get("City", city_id)
    if one_city is None:
        abort(404)
    json_data = request.get_json()
    if not json_data:
        return jsonify({"message": "Not a JSON"}), 400
    ignore_keys = ['id', 'created_at', 'updated_at']
    for key, value in json_data.items():
        if key not in ignore_keys:
            setattr(one_city, key, value)
    one_city.save()
    json_city = one_city.to_json()
    return jsonify(json_city), 200
