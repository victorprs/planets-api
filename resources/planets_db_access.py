from pymongo import MongoClient
from planetsapi.resources import db_configs
from bson import ObjectId


class PlanetsDbAccess:

    def __init__(self):
        self.client = MongoClient(db_configs.DB_HOST, db_configs.DB_PORT)
        self.db = self.client[db_configs.DB_NAME]

    def insert_planet(self, planet):
        result = self.db.planets.insert_one(planet)
        return result.inserted_id
    
    def find_all(self):
        result = self.db.planets.find()
        return result

    def find_by_id(self, object_id):
        result = self.db.planets.find({"_id": ObjectId(object_id)})
        return result
