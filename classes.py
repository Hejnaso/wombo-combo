

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

    def get_position(self):
        return 0,0

class Planet(CelestialBody):
    def __init__(self, diameter, position, color, name, orbit, angular_speed, orbital_direction):
        super().__init__(diameter, position, color, name)
        self.orbit = orbit
        self.angular_speed = angular_speed
        self.orbital_direction = orbital_direction
        print("{} created".format(self.name))

    def get_position(self):
        return (self.orbit.radius*cos(radians(self.position)),self.orbit.radius*sin(radians(self.position)))

    def do_orbital_step(self):
        self.position += self.angular_speed*self.orbital_direction

class Orbit:
    def __init__(self, radius):
        self.radius = radius


class SimulationOfSolarSystem:
    def __init__(self, solar_system, turtle):
        self.solar_system = solar_system
        self.turtle = turtle
        self.turtle.speed(0)
        self.turtle.tracer(0,0)

    def draw_planet(self, planet):
        turtle.penup()
        self.turtle.setpos(planet.get_position())
        turtle.pendown()
        self.turtle.dot(planet.diameter, planet.color)

    def draw_orbit(self, orbit):
        turtle.penup()
        self.turtle.setpos(self.solar_system.star.get_position()[0],-orbit.radius)
        #self.setpos = turtle_setpos
        turtle.pendown()
        self.turtle.circle(orbit.radius)

    def draw_star(self, star):
        turtle.penup()
        self.turtle.setpos(star.get_position())
        turtle.pendown()
        self.turtle.dot(star.diameter, star.color)

    def draw_hole(self):
        turtle.penup()
        self.turtle.setpos(20,20)
        turtle.pendown()
        self.turtle.dot(30, "grey")

    def step(self):

        for planet in self.solar_system.planets:
            planet.do_orbital_step()

    def run(self):
        while True:
            self.turtle.clear()
            self.show()
            turtle.update()
            self.step()


    def show(self):
        self.draw_star(self.solar_system.star)
        self.draw_hole()
        for planet in self.solar_system.planets:
            self.draw_planet(planet)
            self.draw_orbit(planet.orbit)



def main():

    sun = Star(diameter=100,position=(0,0),color="black",name="Death Star")

    orbit_mercury = Orbit(radius=100)
    orbit_venus = Orbit(radius=160)
    orbit_earth = Orbit(radius=250)
    orbit_mars = Orbit(radius=350)

    mercury = Planet(diameter=10,position=0,color="orange", name="Mercury", orbit=orbit_mercury, angular_speed=3, orbital_direction=1)
    venus = Planet(diameter=15, position=0, color="yellow", name="Venus", orbit=orbit_venus, angular_speed=4, orbital_direction=1)
    earth = Planet(diameter=20, position=0, color="blue", name="Earth", orbit=orbit_earth, angular_speed=5, orbital_direction=1)
    mars = Planet(diameter=17, position=0, color="red", name="Mars", orbit=orbit_mars, angular_speed=6, orbital_direction=1)


    solar_system = SolarSystem(name="Solar system", planets=[mercury, venus, earth, mars], star=sun)
    simulation = SimulationOfSolarSystem(turtle=turtle, solar_system=solar_system)

    simulation.run()


    turtle.exitonclick()

main()