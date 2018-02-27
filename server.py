from flask import Flask
from flask_restful import Api
from planetsapi.resources.planets import Planets, PlanetById

app = Flask(__name__)
api = Api(app)

api.add_resource(Planets, '/planets')
api.add_resource(PlanetById, '/planets/<string:object_id>')
