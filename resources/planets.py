from flask_restful import Resource

class Planets(Resource):
    # def Planets(self, parser):
    #     self.parser = parser

    def get(self):
        return "Tatooine"

    # def post(self):
    #     args = parser.parse_args()
    #     return 