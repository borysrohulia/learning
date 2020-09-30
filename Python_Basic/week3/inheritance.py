import json

class Pet:
    def __init__(self, name=None):
        self.name = name

class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        # super(ExDog, self).__init__(name)
        self.breed = breed
    
    def say(self):
        return "{0}: waw".format(self.name)

dog = Dog('Шарик', 'Добреман')

print(dog.name)
print(dog.say())

class ExportJSON:
    def to_json(self):
        return json.dumps({
            "name": self.name,
            "breed": self.breed
        })

class ExDog(Dog, ExportJSON):
    pass

new_dog = ExDog("Белка", breed="Дворняжка")

print(new_dog.to_json())

print(issubclass(int, object))
print(issubclass(Dog, object))
print(issubclass(Dog, Pet))
print(issubclass(Dog, int))
print(isinstance(dog, Dog))
print(isinstance(dog, Pet))
print(isinstance(dog, object))

print(ExDog.__mro__)

class WoolenDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        #  явное указнание метода конкретного класса
        super(Dog, self).__init__(name)
        self.breed = "Шерстяная собака породы {0}".format(breed)

dog_3 = WoolenDog("Жучка", breed="Такса")
print(dog_3.breed)

class Dog_2(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.__breed = breed

    def say(self):
        return "{0}: waw!".format(self.name)

    def get_breed(self):
        return self.__breed

class ExDog_2(Dog_2, ExportJSON):
    def get_breed(self):
        return "порода: {0} - {1}".format(self.name, self.__breed)
        # return "порода: {0} - {1}".format(self.name, self._Dog_2__breed)

doggg = ExDog_2("Фокс", "Мопс")
print(doggg.__dict__)
print(doggg.get_breed())