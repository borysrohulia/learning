class Human:
    pass

class Robot:
    """Данный класс позволяет создавать роботоа"""

print(Robot)
print(dir(Robot))

class Planet:
    pass

planet = Planet()

print(planet)

solar_system = []

for i in range(8):
    planet = Planet()
    solar_system.append(planet)

print(solar_system)

solar_system2 = {}


for i in range(8):
    planet = Planet()
    solar_system2[planet] = True

print(solar_system2)

class True_Planet:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return f"Planet {self.name}"

earth = True_Planet("Earth")
print(earth)

normal_solar_system = []

planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

for name in planet_names:
    planet = True_Planet(name)
    normal_solar_system.append(planet)

print(normal_solar_system)

mars = True_Planet("Mars")

mars.name = "second earth"

print(mars)

# del mars.name  -          удаляет атрибут класса