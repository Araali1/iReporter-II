from flask import jsonify
from datetime import date
import uuid

events_list = []

class Event(object):
    """class that deals with events data"""

    def __init__(self):
        self.events_list = events_list
       
       # Method for creating an event
    def create(self, eventType, comment, createdBy, location):
        event_details = {}
        event_details["id"] = len(events_list) + 1
        event_details["CreatedOn"] = date.today()
        event_details["createdBy"] = createdBy
        event_details["eventType"] = eventType
        event_details["location"] = location
        event_details["status"] = "pending"
        event_details["comment"] = comment

        events_list.append(event_details)
        events = len(self.events_list)
        print(events)
        newEvent = self.events_list[events - 1]
        return jsonify({
           "status": 201,
           "message": "Created succesfully",
           "data": newEvent
        })
    
    # To get all incidents
    def get_all(self):
        return jsonify({
            "events": self.events_list
        })

    def getBy_id(self, id):
        for item in events_list:
            if item['eventType'] == 'redflag' and item['id']==int(id):
                return item
        return 'Sorry, No record yet by this id'

    def checkEvent(self, id):
        for item in events_list:
            if item['eventType'] == 'redflag' and item['id']==int(id):
                return True
        return False

    def editLocation(self, id, attribute):
        if self.checkEvent(id):
            item = self.getBy_id(id)
            item['location'] = attribute
            return jsonify({
               "status": 201,
               "message": "Patched successfully",
               "data": self.getBy_id(id)
           })
        return jsonify({
            "status": 400,
            "message": "Record with that ID does not exist." 
            })

    def editComment(self, id, attribute):
        if self.checkEvent(id):
            item = self.getBy_id(id)
            item['comment'] = attribute
            return jsonify({
               "status": 201,
               "message": "Patched successfully",
               "data": self.getBy_id(id)
           })
        return jsonify({
            "status": 400,
            "message": "Record with that ID does not exist." 
            })       
    def deleteEvent(self, id):
        if self.checkEvent(id):
            for item in events_list:
                if item['id'] == int(id):
                    events_list.pop(events_list.index(item))
                    return jsonify({
                        "status": 201,
                        "data": [{
                            "id": id,
                            "message": "You have delete a record"
                        }]
                    })
        return jsonify({
            "status": 400,
            "message": "Record with this id nolonger exists"
        })