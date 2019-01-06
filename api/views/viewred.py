from flask import jsonify, request
#from api.v1 import v1
from flask import Blueprint

app = Blueprint('app', __name__)

@app.route('/')
def index():
    return jsonify({'message': 'Okay, Stunts. Great guy'})