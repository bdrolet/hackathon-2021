from flask import Flask
from app.routes.api import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)
