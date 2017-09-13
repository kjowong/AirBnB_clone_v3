#!/usr/bin/python3
"""
    states.py file in v1/views
"""
from flask import Flask, jsonify
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
    state_list = []
    all_states = storage.all('State')
    for object in all_states.values():
        state_list.append(to_json(object))
    return (jsonify(state_list))

@app_views.route("/states/<string:state_id>", methods=['GET'])
def get_a_state():
    """
        Method to return a JSON representation of a state
    """
    one_state = storage.get("State", state_id)
    if one_state is None:
        abort(404)
    else:
        return (to_json(one_state))

@app_views.route("/states/<string:state_id>", methods=['DELETE'])
def delete_a_state():
    """
        Method to delete a state
    """
    to_delete = storage.get("State", state_id)
    if to_delete is None:
        abort(404)
    else:
        storage.delete(to_delete)
        response = to_json({})
        response.status = 200
        return response
