from flask import Blueprint
from flask_restful import Resource, Api

from app.api.v1.views.viewred import Events

v1 = Blueprint('v1', __name__, url_prefix='/api/v1')
api=Api(v1)

api.add_resource(Events, '/events')
# api.add_resource(RedFlags, '/redflags/<id>')

#api = Blueprint('api', __name__)

#from app.api.views import viewred