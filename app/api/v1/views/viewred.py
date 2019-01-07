from flask import jsonify, request, make_response
from flask_restful import Resource
from app.api.v1.models.redflags import Event as EventModel

#from app.api import api

#@api.route('/')
#def index():
#    return jsonify({'message': 'Okay, Araali1. Lets go, it fun'}), 200

class Events(Resource):
    def __init__(self):
        self.eventObject = EventModel()

        #starting to create an Event - POST
    def post(self):
        events_data = request.get_json()
        eventType = events_data["eventType"]
        comment = events_data["comment"]
        createdBy = events_data["createdBy"]
        location = events_data["location"]
       
        response = self.eventObject.create(eventType, comment, createdBy, location)
        return response
    
    def get(self):
        response = self.eventObject.get_all() 
        return response

class RedFlags(Resource):
    def __init__(self):
        self.eventObject = EventModel

    def get(self, id):
        response = self.eventObject.getBy_id(self, id)
        return make_response(jsonify(response))