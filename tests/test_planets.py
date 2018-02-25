from planetsapi.resources.planets import Planets, PlanetByName, PlanetById

import unittest

class PlanetsTest(unittest.TestCase):
    def test_1_equal_1(self):
        assert 1 == 1

    def test_get_tatooine(self):
        planets = Planets()
        assert planets.get() == "Tatooine"

    def test_get_planet_by_name(self):
        planets = PlanetByName()
        assert planets.get("Tatooine") == "Tatooine"

    def test_get_planet_by_id(self):
        planets = PlanetById()
        assert planets.get(12) == 12

    def test_delete_planet_by_id(self):
        planets = PlanetById()
        assert planets.delete(12) == ('', 204)
