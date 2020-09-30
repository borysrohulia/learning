class Planet:
    count = 0

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []
        Planet.count += 1

earth = Planet("Earth")
mars = Planet("Mars")

print(Planet.count)
print(mars.count)

class Human:
    def __del__(self):
        print("Goodbye!")

human = Human()

del human

class Planet2:
    count = 0

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []

planet = Planet2("Earth")

print(planet.__dict__)

planet.mass = 5.97e24

print(planet.__dict__)

print(Planet2.__dict__)
print(Planet2.__doc__)
print(dir(planet))
print(planet.__class__)

class Planet3:
    def __new__(cls, *args, **kwargs):
        print("__new__ called")
        obj = super().__new__(cls)
        return obj

    def __init__(self, name):
        print("__init__ called")
        self.name = name

my_earth = Planet3("Earth")