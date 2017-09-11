#!/usr/bin/python3
"""
    index.py file in v1/views
"""
from flask import Flask, jsonify
from api.v1.views import app_views
app = Flask(__name__)


@app_views.route("/status")
def status_message():
    return jsonify({"status": "OK"})
