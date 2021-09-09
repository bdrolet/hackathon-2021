from flask import Flask
from flask_cors import CORS
from app.routes.api import blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(blueprint)
