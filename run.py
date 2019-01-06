import os
from api import create_app
from instance.config import app_config

config_name = os.getenv('FLASK_ENV')
app = create_app(app_config['development'])

if __name__ == '__main__':
    app.run(debug=True)