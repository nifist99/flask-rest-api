from flask import Flask,Blueprint
from markupsafe import escape
import sys
from flask_wtf import CSRFProtect

csrf = CSRFProtect()
# load modules
from api.users import blueprint_users


app = Flask(__name__)

csrf.init_app(app)
app.config.from_mapping({'WTF_CSRF_ENABLED':False})

# register blueprints. ensure that all paths are versioned!
app.register_blueprint(csrf.exempt(blueprint_users), url_prefix="/api/v1/users")