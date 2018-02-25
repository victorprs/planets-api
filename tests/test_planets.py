from planetsapi.resources.planets import Planets
def test_1_equal_1():
    assert 1 == 1

def test_get_tatooine():
    planets = Planets()
    assert planets.get() == "Tatooine"