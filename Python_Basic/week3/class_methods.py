from datetime import date

class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

class Planet:
    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []

    def add_human(self, human):
        print(f'Welocme to {self.name}, {human.name}!')
        self.population.append(human)


mars = Planet("Mars")
bob = Human("Bob")

mars.add_human(bob)

print(mars.population)

class Human_2:
    def __init__(self, name, age=0):
        self._name = name
        self._age = age

    def _say(self, text):
        print(text)

    def say_name(self):
        self._say(f"Hello, I am {self._name}")

    def say_how_old(self):
        self._say(f"I am {self._age} years old")

vasya = Human_2("Vasya", age=29)

vasya.say_name()
vasya.say_how_old()

def extract_description(user_string):
    return "открытие чемпионата мира по футболу"

def extract_date(user_string):
    return date(2018, 6, 14)

class Event:
    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date
    
    def __str__(self):
        return f"Event \"{self.description}\" at {self.date}"

    @classmethod
    def from_string(cls, user_input):
        description = extract_description(user_input)
        date = extract_date(user_input)
        return cls(description, date)


# event_description = "Рассказать о себе"
# event_date = date.today()

# event = Event(event_description, event_date)

event = Event.from_string('add to calendar opening world championship at 14 june 2018')

print(event)

print(dict.fromkeys("12345"))