from flask import jsonify, request, make_response
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
           "message": "Your record has been created",
           "data": newEvent
        })
    
"""    # To get all incidents
    def get_all(self):
        return jsonify({
            "events": self.events_list
        })

    def getBy_id(self, id):
        for item in events_list:
            if item['eventType']=='redflag' and item['id']==int(id):
                print('ddffgg')
                return item
        return 'Sorry, No record yet' """