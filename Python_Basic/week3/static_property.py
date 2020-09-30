class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    @staticmethod
    def is_age_valid(age):
        return 0 < age < 150

print(Human.is_age_valid(35))

human = Human("Old Bobby")
print(human.is_age_valid(350))

class Robot:
    def __init__(self, power):
        self.power = power

wall_e = Robot(100)
print(wall_e.power)
wall_e.power = 200
print(wall_e.power)
wall_e.power = -20

#  second example

class Robot_2:
    def __init__(self, power):
        self.power = power

    def set_power(self, power):
        if power < 0:
            self.power = 0
        else:
            self.power = power

wall_e = Robot_2(100)
wall_e.set_power(-20)
print(wall_e.power)

#  third example

class Robot_3:
    def __init__(self, power):
        self._power = power

    power = property()

    @power.setter
    def power(self, value):
        if value < 0:
            self._power = 0
        else:
            self._power = value

    @power.getter
    def power(self):
        return self._power

    @power.deleter
    def power(self):
        print('make robot useless')
        del self._power

wall_e = Robot_3(100)
wall_e.power = -20
print(wall_e.power)
del wall_e.power

# fourth example

class Robot_4:
    def __init__(self, power):
        self._power = power

    @property
    def power(self):
        """тут могут быть любые вычисления"""
        return self._power