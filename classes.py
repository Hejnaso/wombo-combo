

import turtle
import time
from math import cos, sin, radians


class SolarSystem:
    def __init__(self, name, planets, star):
        self.name = name
        self.planets = planets
        self.star = star
        print("{} created".format(self.name))

class CelestialBody:
    def __init__(self, diameter, position, color, name):
        self.diameter = diameter
        self.position = position
        self.color = color
        self.name = name

class Star(CelestialBody):
    def __init__(self, diameter, position, color, name):
        super().__init__(diameter, position, color, name)
        print("{} created".format(self.name))

class Planet(CelestialBody):
    def __init__(self, diameter, position, color, name, orbit):
        super().__init__(diameter, position, color, name)
        self.orbit = orbit
        print("{} created".format(self.name))

class Orbit:
    def __init__(self, radius):
        self.radius = radius

class SimulationOfSolarSystem:
    def __init__(self, solar_system, turtle):
        self.solar_system = solar_system
        self.turtle = turtle

    def show(self):
        #for planet in self.solar_system.planets:
        #    turtle.pendown()
        #    turtle.posit

        turtle.exitonclick()

def main():

    sun = Star(diameter=100,position=(0,0),color="black",name="Death Star")

    orbit_mercury = Orbit(radius=300)
    orbit_venus = Orbit(radius=400)
    orbit_earth = Orbit(radius=500)
    orbit_mars = Orbit(radius=600)


    mercury = Planet(diameter=10,position=0,color="orange", name="Mercury", orbit=orbit_mercury)
    venus = Planet(diameter=15, position=0, color="yellow", name="Venus", orbit=orbit_venus)
    earth = Planet(diameter=20, position=0, color="blue", name="Earth", orbit=orbit_earth)
    mars = Planet(diameter=17, position=0, color="red", name="Mars", orbit=orbit_mars)


    solar_system = SolarSystem(name="Solar system", planets=[mercury, venus, earth, mars], star=sun)
    simulation = SimulationOfSolarSystem(turtle=turtle, solar_system=solar_system)

main()