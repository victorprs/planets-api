from flask import Flask
from flask_restful import Api
from planetsapi.resources.planets import Planets

app = Flask(__name__)
api = Api(app)

api.add_resource(Planets, '/planets')