#!/usr/bin/python3
"""
    states.py file in v1/views
"""
from flask import abort, Flask, jsonify
from api.v1.views import app_views
from models import storage
from models.base_model import BaseModel

# is this next line needed? we are never using app, only app_views
app = Flask(__name__)
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
    for object in all_states.values():
        # to_json() the object and append to the list
        state_list.append(to_json(object))
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
        return (jsonify(to_json(one_state)))


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
        # Set response status code
        response.status = 200
        # return response
        return response
