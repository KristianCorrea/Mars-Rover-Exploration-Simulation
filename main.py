import math

from planet_intel import PlanetIntel
from rover import Rover

planet_1 = PlanetIntel.get_planet_1()
planet_2 = PlanetIntel.get_planet_2()
planet_3 = PlanetIntel.get_planet_3()

def map_surface(planet):
    # Creates a rover on the planet_1 surface with an unlimited battery
    rover = Rover(planet, math.inf)

    pass

def map_surface_with_battery_constraint(planet):
    rover = Rover(planet, 20)

    pass

