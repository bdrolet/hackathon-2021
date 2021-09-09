from flask import Flask
from flask_cors import CORS
import marshmallow
from app.routes.api import blueprint
from flask_marshmallow import Marshmallow

app = Flask(__name__)
CORS(app)
ma = Marshmallow(app)

app.register_blueprint(blueprint)
