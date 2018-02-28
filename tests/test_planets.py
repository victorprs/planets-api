import unittest
import os
from planetsapi.server import app


class PlanetsTest(unittest.TestCase):
    def setUp(self):
        os.system("mongo < tests/BuildDbTestScript.js")
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

    def test_post_planet_with_no_correspodent_on_swapi(self):
        response = self.app.post('/planets', data=dict(
            name="Starkiller",
            climate="frozen",
            terrain="mountains"
        ))
        assert 201 == response.status_code

    def test_get_planet_by_id(self):
        response = self.app.get('/planets?object_id=5a959ef17ef03fc0da5bc177')
        assert b'"name": "Tatooine", "climate": "arid", "terrain": "desert"' in response.data

    def test_get_planet_by_inexistent_id_return_404(self):
        response = self.app.get('/planets?object_id=4a959ef17ef03fc0da5bc177')
        assert 404 == response.status_code

    def test_get_planet_by_invalid_id_return_400(self):
        response = self.app.get('/planets?object_id=123456')
        assert 400 == response.status_code

    def test_get_planet_by_id_and_name_return_400(self):
        response = self.app.get('/planets?object_id=123456&name=abc')
        assert 400 == response.status_code

    def test_get_planet_by_name(self):
        response = self.app.get('/planets?name=Tatooine')
        assert b'"name": "Tatooine", "climate": "arid", "terrain": "desert"' in response.data

    def test_get_planet_by_inexistent_name_return_404(self):
        response = self.app.get('/planets?name=Bob')
        assert 404 == response.status_code

    def test_delete_planet_by_id_return_204_no_content(self):
        response = self.app.delete('/planets/5a959ef17ef03fc0da5bc177')
        assert 204 == response.status_code

    def test_delete_planet_by_invalid_id_return_400(self):
        response = self.app.delete('/planets/asdfasdf')
        assert 400 == response.status_code
