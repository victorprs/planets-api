from flask_restful import Resource, reqparse
from bson.errors import InvalidId
from planetsapi.resources.planets_db_access import PlanetsDbAccess


class Planets(Resource):
    def __init__(self):
        self.planets_dao = PlanetsDbAccess()

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('object_id', type=str, location='args')
        parser.add_argument('name', type=str, location='args')
        args = parser.parse_args()
        name_value = args['name']
        obj_id_value = args['object_id']

        if name_value and obj_id_value:
            return 'Search for id OR for name', 400
        elif obj_id_value:
            return self.get_by_id(obj_id_value)
        elif name_value:
            return self.get_by_name(name_value)
        return self.get_all()

    def get_all(self):
        cursor = self.planets_dao.find_all()

        result = []
        for planet in cursor:
            planet['object_id'] = str(planet['_id'])
            planet.pop('_id')
            print(type(planet))
            result.append(planet)
        return result

    def get_by_id(self, object_id):
        try:
            planet = self.planets_dao.find_by_id(object_id).next()
            planet['object_id'] = str(planet['_id'])
            planet.pop('_id')
            return planet
        except InvalidId:
            return object_id + ' is not a valid ObjectId, it must be a 12-byte input or a 24-character hex string', 400
        except StopIteration:
            return object_id + ' was not found', 404

    def get_by_name(self, name):
        try:
            planet = self.planets_dao.find_by_name(name).next()
            planet['object_id'] = str(planet['_id'])
            planet.pop('_id')
            return planet
        except StopIteration:
            return name + ' was not found', 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('climate')
        parser.add_argument('terrain')
        args = parser.parse_args()
        object_id = self.planets_dao.insert_planet(args)
        return str(object_id), 201


class PlanetById(Resource):

    def delete(self, object_id):
        return '', 204
