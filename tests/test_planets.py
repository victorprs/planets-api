import unittest
from planetsapi.server import app


class PlanetsTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_planets(self):
        response = self.app.get('/planets')
        assert b'"name": "Tatooine", "climate": "arid", "terrain": "desert"' in response.data
        assert b'"name": "Coruscant", "climate": "humid", "terrain": "cityscape"' in response.data
        assert b'"name": "Hoth", "climate": "frozen", "terrain": "ice caves"' in response.data

    def test_post_planet(self):
        response = self.app.post('/planets', data=dict(
            name="Kamino",
            climate="temperate",
            terrain="ocean"
        ))
        assert 201 == response.status_code

    def test_get_planet_by_name(self):
        response = self.app.get('/planets/Tatooine')
        assert b'Tatooine' in response.data

    def test_get_planet_by_id(self):
        response = self.app.get('/planets/12')
        assert b'12' in response.data

    def test_delete_planet_by_id(self):
        response = self.app.get('/planets/12')
        assert b'' in response.data
