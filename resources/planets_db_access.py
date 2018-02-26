from pymongo import MongoClient


class PlanetsDbAccess:

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.swapi

    def insert_planet(self, planet):
        result = self.db.planets.insert_one(planet)
        return result.inserted_id
