from flask import Flask


def create_app(config_name):
    app = Flask(__name__)
    
    from api.views.viewred import app as version_one
    app.register_blueprint(version_one, url_prefix='/api/v1')
#    app.register_blueprint(version_one, url_prefix='/api/v1')
    return app