#  magic vethods

import random

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):                    # str метод для описания класса
        return '{} <{}>'.format(self.name, self.email)

    def __hash__(self):             # указываем что захешировать
        return hash(self.email)

    def __eq__(self, obj):           # сравнение объектов   
        return self.email == obj.email

    def get_email_data(self):
        return {
            'name': self.name,
            'email': self.email
        }

jane = User("Jane", "abv@gmail.com")
joe = User("joe", "abv@gmail.com")
print(jane == joe)
print(hash(jane))
print(hash(joe))

# если создать объекьт с двумя ключами юзеров, то не получится, т.к. у jane и joe одинаковый хеш

user_email_map = {user: user.name for user in [jane, joe]}

print(user_email_map)

class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

a = Singleton()
b = Singleton()

print(a is b)

# class Reseacher:
#     def __getattr__(self, name):
#         return 'Nothing not found :('

#     def __getattribute__(self, name):
#         return 'nope'


class Reseacher:
    def __getattr__(self, name):            # если атрибут не найден вызывается
        return 'Nothing not found :('

    def __getattribute__(self, name):               # при обращении к атрибуту и не важно существует атрибут или нет
        print('Looking for {}'.format(name)) 
        return object.__getattribute__(self, name)

obj = Reseacher()

print(obj.attr)
print(obj.methods)
print(obj.asd123)

class Ignorator:
    def __setattr__(self, name, value):             # вызывается при установлении атрибута
        print('Not gonna set: {}!'.format(name))

obj_2 = Ignorator()
# obj_2.math = True

# print(obj_2.math)


class Polite:                   # вызывается при установлении удалении
    def __delattr__(self, name):
        value = getattr(self, name)
        print(f'Goodbye {name}, you were {value}!')

        object.__delattr__(self, name)

obj_3 = Polite()

obj_3.attr = 10
del obj_3.attr

class Logger:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, func):               # типа вызов функции при обращении к экземпляру класса
        with open(self.filename, 'w') as f:
            f.write('Oh Danny boy...')
        return func

logger = Logger('log.txt')

@logger
def completly_useless_function():
    pass

completly_useless_function()

with open('log.txt', 'r') as f:
    print(f.read())



class NoisyInt:
    def __init__(self, value):
        self.value = value

    def __add__(self, obj):             # при сложении 
        noise = random.uniform(-1, 1)
        return self.value + obj.value + noise


a = NoisyInt(10)
b = NoisyInt(20)

for _ in range(3):
    print(a+b)


class PascalList:
    def __init__(self, original_list=None):
        self.container = original_list or []

    def __getitem__(self, index):
        return self.container[index - 1]

    def __setitem__(self, index, value):
        self.container[index - 1] = value

    def __str__(self):
        return self.container.__str__()

numbers = PascalList([1,2,3,4,5])

print(numbers[1])