from flask_restful import Resource, reqparse
from planetsapi.resources.planets_db_access import PlanetsDbAccess


class Planets(Resource):
    def __init__(self):
        self.planets_dao = PlanetsDbAccess()

    def get(self):
        cursor = self.planets_dao.find_all()
        result = []
        for planet in cursor:
            planet['object_id'] = str(planet['_id'])
            planet.pop('_id')
            print(type(planet))
            result.append(planet)
        return result

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('climate')
        parser.add_argument('terrain')
        args = parser.parse_args()
        object_id = self.planets_dao.insert_planet(args)
        return str(object_id), 201


class PlanetByName(Resource):

    def get(self, name):
        return name


class PlanetById(Resource):

    def get(self, object_id):
        return object_id

    def delete(self, object_id):
        return '', 204
