#!/usr/bin/python3
"""
    amenity.py file in api/v1/views
"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity

to_json = BaseModel.to_json


@app_views.route('/amenities', methods=['GET'])
def get_all_amenities():
    """
        Method to retrieve a list of all objects
    """
    # Create empty list to add to_json() objects to
    amenity_list = []
    # Get dictionary of all Amenity objects
    all_amenities = storage.all('Amenity')
    # Loop through values in the dictionary
    for amenity_object in all_amenities.values():
        # to_json() the object and append to the list
        amenity_list.append(amenity_object.to_json())
    # jsonify the list and return
    return (jsonify(amenity_list))

    
@app_views.route('/amenities/<string:amenity_id>', methods=['GET'])
def get_an_amenity(amenity_id):
    """
        Method to retrieve an Amenity object
    """
    # Attempt to retrieve the state using amenity_id
    one_amenity = storage.get("Amenity", amenity_id)
    # if amenity doesn't exist, raise 404 error
    if one_amenity is None:
        abort(404)
    # if amenity exists
    else:
        # Return jsonifies to_json'd Amenity object
        return (jsonify(one_amenity.to_json()))


@app_views.route('/amenities/<string:amenity_id>', methods=['DELETE'])
def delete_an_amenity(amenity_id):
    """
        Method to delete an Amenity object
    """
    # Retrieve the Amenity object to delete
    to_delete = storage.get("Amenity", amenity_id)
    # If the Amenity object doesn't exist, raise 404 error
    if to_delete is None:
        abort(404)
    # Amenity object exists
    else:
        # Delete the Amenity object
        storage.delete(to_delete)
        # Create response with an empty dictionary
        response = jsonify({})
        # Return response with status code 200
        return response, 200


@app_views.route('/amenities', methods=['POST'])
def post_an_amenity():
    """
        Method to create an Amenity object
    """
    # Transform HTTP request to dict
    json_data = request.get_json()
    # HTTP request not valid JSON: raise 400 status
    if not json_data:
        return jsonify({"message": "Not a JSON"}), 400
    # Get the value of name in json_data
    name = json_data.get("name")
    # if dict doesn't contain name, raise 400
    if name is None:
        return jsonify({"message": "Missing name"}), 400
    # Create new Amenity instance with data
    new_amenity = Amenity(**json_data)
    # Save new_amenity
    new_amenity.save()
    # Get the json dict of new_amenity
    json_amenity = new_amenity.to_json()
    # returns the new Amenity with status code 201
    return jsonify(json_amenity), 201


@app_views.route('/amenities/<string:amenity_id>', methods=['PUT'])
def put_an_amenity(amenity_id):
    """
        Method to update an Amenity object
    """
    # Retrieve the amenity
    one_amenity = storage.get("Amenity", amenity_id)
    # if the Amenity doesn't exist, raise 404 error
    if one_amenity is None:
        abort(404)
    # Transform HTTP request body into a dictionary
    json_data = request.get_json()
    # if HTTP request not valid JSON, raise 400 error
    if not json_data:
        return jsonify({"message": "Not a JSON"})
    # Create list of keys we don't want updated
    ignore_keys = ['id', 'created_at', 'updated_at']
    # update Amenity obj with all key-value pairs of the dict
    for key, value in json_data.items():
        # Only update keys not found in ignore_keys
        if key not in ignore_keys:
            # Update the Amenity object
            setattr(one_amenity, key, value)
    # Save the Amenity
    one_amenity.save()
    # Call to_json on one_amenity
    json_amenity = one_amenity.to_json()
    # Return Amenity object with status code 200
    return jsonify(json_amenity), 200
