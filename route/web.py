from flask import Flask
import sys

# load modules
from api.users import blueprint_users

app = Flask(__name__)

# register blueprints. ensure that all paths are versioned!
app.register_blueprint(blueprint_users, url_prefix="/api/v1/users")