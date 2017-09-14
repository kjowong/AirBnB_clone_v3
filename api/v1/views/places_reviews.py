#!/usr/bin/python3
"""
    review.py file in v1/views
"""
from flask import abort, Flask, jsonify, request
from api.v1.views import app_views
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.user import User

to_json = BaseModel.to_json


@app_views.route("/places/<string:place_id>/reviews", methods=['GET'])
def get_all_reviews(place_id):
    """
        Method to return a JSON representation of all reviews
    """
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    review_list = []
    for review in place.reviews:
        review_list.append(review.to_json())
    return jsonify(review_list)


@app_views.route("/reviews/<string:review_id>", methods=['GET'])
def get_a_review(review_id):
    """
        Method to return a JSON representation of a review
    """
    one_review = storage.get("Review", review_id)
    if one_review is None:
        abort(404)
    return (jsonify(one_review.to_json()))


@app_views.route("/reviews/<string:review_id>", methods=['DELETE'])
def delete_a_review(review_id):
    """
        Method to delete a review
    """
    to_delete = storage.get("Review", review_id)
    if to_delete is None:
        abort(404)
    else:
        storage.delete(to_delete)
        response = jsonify({})
        return response, 200


@app_views.route("/places/<string:place_id>/reviews", methods=['POST'])
def create_a_review(place_id):
    """
        Method to create a review
    """
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    json_data = request.get_json()
    if not json_data:
        return jsonify({"message": "Not a JSON"}), 400
    user_id = json_data.get("user_id")
    if user_id is None:
        return jsonify({"message": "Missing user_id"}), 400
    user_id_obj = storage.get("User", user_id)
    if user_id_obj is None:
        abort(404)
    text = json_data.get("text")
    if text is None:
        return jsonify({"message": "Missing text"}), 400
    new_review_dict = {}
    new_review_dict.update(json_data)
    new_review_dict["place_id"] = place_id
    new_review = Review(**new_review_dict)
    new_review.save()
    json_review = new_review.to_json()
    return jsonify(json_review), 201


@app_views.route('/reviews/<string:review_id>', methods=['PUT'])
def put_a_review(review_id):
    one_review = storage.get("Review", review_id)
    if one_review is None:
        abort(404)
    json_data = request.get_json()
    if not json_data:
        return jsonify({"message": "Not a JSON"}), 400
    ignore_keys = ['id', 'user_id', 'place_id', 'created_at', 'updated_at']
    for key, value in json_data.items():
        if key not in ignore_keys:
            setattr(one_review, key, value)
    one_review.save()
    json_review = one_review.to_json()
    return jsonify(json_review), 200
