#!/usr/bin/python3
"""
    states.py file in v1/views
"""
from flask import abort, Flask, jsonify, request
from api.v1.views import app_views
from models import storage
from models.base_model import BaseModel
from models.state import State

to_json = BaseModel.to_json


@app_views.route("/states", methods=['GET'])
def get_all_states():
    """
        Method to return a JSON representation of all states
    """
    # Create empty list to add to_json() objects to
    state_list = []
    # Get dictionary of all State objects
    all_states = storage.all('State')
    # Loop through values in the dictionary
    for state_object in all_states.values():
        # to_json() the object and append to the list
        state_list.append(to_json(state_object))
    # jsonify the list and return
    return (jsonify(state_list))


@app_views.route("/states/<string:state_id>", methods=['GET'])
def get_a_state(state_id):
    """
        Method to return a JSON representation of a state
    """
    # Attempt to retrieve the state using state_id
    one_state = storage.get("State", state_id)
    # If state doesn't exist, return a 404 error
    if one_state is None:
        abort(404)
    # State exists
    else:
        # Return jsonified to_json'd state object
        return (jsonify(one_state.to_json()))


@app_views.route("/states/<string:state_id>", methods=['DELETE'])
def delete_a_state(state_id):
    """
        Method to delete a state
    """
    # Retrieve the State object to delete
    to_delete = storage.get("State", state_id)
    # If the State object doesn't exist, return 404 error
    if to_delete is None:
        abort(404)
    else:
        # Delete the State object
        storage.delete(to_delete)
        # Create response with an empty dictionary
        response = jsonify({})
        # return response
        return response, 200


@app_views.route("/states", methods=['POST'])
def create_a_state():
    """
        Method to create a state
    """
    # Get data from request
    json_data = request.get_json()
    # Error out if no data or if no name provided
    if not json_data:
        return jsonify({"message": "Not a JSON"}), 400
    name = json_data.get("name")
    if name is None:
        return jsonify({"message": "Missing name"}), 400
    # Create new State instance with data
    new_state = State(**json_data)
    # Save new_state
    new_state.save()
    # Get the json dict of new_state
    json_state = new_state.to_json()
    # Return jsonified info with status 201
    return jsonify(json_state), 201


@app_views.route('/states/<string:state_id>', methods=['PUT'])
def put_a_state(state_id):
    # Retrieve the state
    one_state = storage.get("State", state_id)
    # Return with error if state doesn't exist
    if one_state is None:
        abort(404)
    # Get dict of attributes in request
    json_data = request.get_json()
    # Check json_data
    if not json_data:
        return jsonify({"message": "Not a JSON"}), 400
    # Create list of keys we don't want updated
    ignore_keys = ['id', 'created_at', 'updated_at']
    # Loop through the json_data, update/add keys
    for key, value in json_data.items():
        # Only update certain attributes
        if key not in ignore_keys:
            # Update State object
            setattr(one_state, key, value)
    # Save the state
    one_state.save()
    # Call to_json on one_state
    json_state = one_state.to_json()
    # Return jsonified json_state with status 200
    return jsonify(json_state), 200
