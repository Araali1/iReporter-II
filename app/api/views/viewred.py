from flask import jsonify, request, make_response

from app.api import api

@api.route('/')
def index():
    return jsonify({'message': 'Okay, Araali1. Lets go, it fun'}), 200
