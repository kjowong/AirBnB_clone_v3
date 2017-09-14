#!/usr/bin/python3
"""
    First endpoint(route) to return the status of the API
"""
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)

cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def handle_teardown(self):
    """
        method to handle teardown
    """
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """
        Method to handle 404 errors
    """
    message = {
        "error": "Not found"
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = os.getenv("HBNB_API_PORT", "5000")
    app.run(host, port)
