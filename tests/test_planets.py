import unittest
from planetsapi.server import app


class PlanetsTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_planets(self):
        response = self.app.get('/planets')
        assert b'[]' in response.data

    def test_get_planet_by_name(self):
        response = self.app.get('/planets/Tatooine')
        assert b'Tatooine' in response.data

    def test_get_planet_by_id(self):
        response = self.app.get('/planets/12')
        assert b'12' in response.data

    def test_delete_planet_by_id(self):
        response = self.app.get('/planets/12')
        assert b'' in response.data
