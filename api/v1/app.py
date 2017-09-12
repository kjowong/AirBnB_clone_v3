#!/usr/bin/python3
"""
    First endpoint(route) to return the status of the API
"""
from flask import Flask
from models import storage
from api.v1.views import app_views
app = Flask(__name__)
app.register_blueprint(app_views)

HBNB_API_HOST = "0.0.0.0"
HBNB_API_PORT = "5000"


@app.teardown_appcontext
def handle_teardown(self):
    """
        method to handle teardown
    """
    storage.close()


if __name__ == "__main__":
    app.run(HBNB_API_HOST, HBNB_API_PORT)

@app.errorhandler(404)
def page_not_found(e):
    """
        Method to handle 404 errors
    """
    return jsonify({"error": "Not found"})
