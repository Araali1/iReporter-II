from flask import jsonify, request, make_response
from flask_restful import Resource
from app.api.v1.models.redflags import Event as EventModel

#from app.api import api
eventObject = EventModel()

#@app.route('/')
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
        image = events_data["image"]
        createdBy = events_data["createdBy"]
        location = events_data["location"]
       
        response = self.eventObject.create(eventType, comment, createdBy, location, image)
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

    def delete(self, id):
        response = eventObject.deleteEvent(id)
        return make_response(response)

class EventDetail(Resource):
    def __init__(self):
        self.EventObject = EventModel       

    def patch(self, id, attribute):
        patch_attributes = ['comment', 'location']
        print(attribute)
        if attribute in patch_attributes:
            patch_data = request.get_json()
            if attribute in patch_data:
                if attribute == "location":
                    result = eventObject.editLocation(id, patch_data['location'])
                    return make_response(result)
                result = eventObject.editComment(id, patch_data['comment'])
                return make_response(result)
            return make_response(jsonify({
            "Status": 403, 
            "message": "Please provide " + attribute  
            }))
        return make_response(jsonify({
            "Status": 403,
            "message": "You can only patch location or comment."
        }), 403)
