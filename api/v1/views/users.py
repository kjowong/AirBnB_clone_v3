#!/usr/bin/python3
"""
    user.py file in v1/views
"""
from flask import abort, Flask, jsonify, request
from api.v1.views import app_views
from models import storage
from models.base_model import BaseModel
from models.user import User

to_json = BaseModel.to_json


@app_views.route("/users", methods=['GET'])
def get_all_users():
    """
        Method to return a JSON representation of all users
    """
    user_list = []
    all_users = storage.all("User")
    for user_object in all_users.values():
        user_list.append(user_object.to_json())
    return (jsonify(user_list))


@app_views.route("/users/<string:user_id>", methods=['GET'])
def get_a_user(user_id):
    """
        Method to return a JSON representation of a user
    """
    one_user = storage.get("User", user_id)
    if one_user is None:
        abort(404)
    return (jsonify(one_user.to_json()))


@app_views.route("/users/<string:user_id>", methods=['DELETE'])
def delete_a_user(user_id):
    """
        Method to delete a user
    """
    to_delete = storage.get("User", user_id)
    if to_delete is None:
        abort(404)
    else:
        storage.delete(to_delete)
        response = jsonify({})
        return response, 200


@app_views.route("/users", methods=['POST'])
def create_a_user():
    """
        Method to create a user
    """
    json_data = request.get_json()
    if not json_data:
        return jsonify({"message": "Not a JSON"}), 400
    email = json_data.get("email")
    if email is None:
        return jsonify({"message": "Missing email"}), 400
    password = json_data.get("password")
    if password is None:
        return jsonify({"message": "Missing password"}), 400
    new_user = User(**json_data)
    new_user.save()
    json_user = new_user.to_json()
    return jsonify(json_user), 201


@app_views.route('/users/<string:user_id>', methods=['PUT'])
def put_a_user(user_id):
    one_user = storage.get("User", user_id)
    if one_user is None:
        abort(404)
    json_data = request.get_json()
    if not json_data:
        return jsonify({"message": "Not a JSON"}), 400
    ignore_keys = ['id', 'email', 'created_at', 'updated_at']
    for key, value in json_data.items():
        if key not in ignore_keys:
            setattr(one_user, key, value)
    one_user.save()
    json_user = one_user.to_json()
    return jsonify(json_user), 200
