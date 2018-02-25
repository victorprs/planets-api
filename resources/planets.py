from flask_restful import Resource, reqparse

class Planets(Resource):
    def get(self):
        return "Tatooine"

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('climate')
        parser.add_argument('terrain')
        args = parser.parse_args()
        return args, 201

class PlanetByName(Resource):

    def get(self, name):
        return name

class PlanetById(Resource):

    def get(self, id):
        return id

    def delete(self, id):
        return '', 204
