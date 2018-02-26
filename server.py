from flask import Flask
from flask_restful import Api
from planetsapi.resources.planets import Planets, PlanetByName, PlanetById

app = Flask(__name__)
api = Api(app)

api.add_resource(Planets, '/planets')
api.add_resource(PlanetById, '/planets/<int:object_id>')
api.add_resource(PlanetByName, '/planets/<string:name>')
