from flask import Blueprint
from flask_restful import Resource, Api

from app.api.v1.views.viewred import Events, RedFlags, EventDetail

v1 = Blueprint('v1', __name__, url_prefix='/api/v1')
api=Api(v1)

api.add_resource(Events, '/events')
api.add_resource(RedFlags, '/redflags/<id>')
api.add_resource(EventDetail, '/redflags/<id>/<attribute>')