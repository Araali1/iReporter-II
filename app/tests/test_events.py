import unittest
from flask import json
from app import create_app
from instance.config import testingConfig

from app.api.v1.models.redflags import events_list

class EventsTest(unittest.TestCase):
    def setUp(self):
        self.event = {
            "eventType": "redflag",
            "comment" : "Araali1, testing",
            "createdBy" : 2,
            "location" : "Adjumani"
        }
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def create_test_record(self):
        self.client.post('/api/v1/events', data=json.dumps(self.event), content_type='application/json')

    def test_create_event_success(self):
        resp = self.client.post('/api/v1/events', data=json.dumps(self.event), content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['message'], "Created succesfully")

    def test_can_get_all_events(self):
        self.create_test_record()
        resp = self.client.get('/api/v1/events')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(data['events']), 1)

    def test_can_patch_a_location(self):
        self.create_test_record()
        patch_data = {
            "location": "Katanga"
        }
        resp = self.client.patch('/api/v1/redflags/1/location', data=json.dumps(patch_data), content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(data['message'], 'Patched successfully')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['data']['location'], 'Katanga')

    def test_can_patch_a_comment(self):
        self.create_test_record()
        patch_data = {
            "comment": "I have seen a corrupt officer"
        }
        resp = self.client.patch('/api/v1/redflags/1/comment', data=json.dumps(patch_data), content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(data['message'], 'Patched successfully')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['data']['comment'], 'I have seen a corrupt officer')

    def test_can_not_patch_non_existent_record(self):
        self.create_test_record()
        patch_data = {
            "location": "Makindye"
        }
        resp = self.client.patch('/api/v1/redflags/5/location', data=json.dumps(patch_data), content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(data['message'], 'Record with that ID does not exist.')
        self.assertEqual(data['status'], 404)

"""    def test_get_event_by_id(self):
        self.create_test_record()
        resp = self.client.get('/api/v1/redflags/1')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(events_list), 5)
        self.assertEqual(data['data'][0]['id'], 1) """