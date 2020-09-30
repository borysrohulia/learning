from functools import reduce
from functools import partial

def caller(func, params):
    return func(*params)

def printer(name, origin):
    print('I\'am {} of {}!'.format(name, origin))

caller(printer, ['Moana', 'Motunui'])

def get_multiplier():
    def inner(a, b):
        return a * b
    return inner

multiplier = get_multiplier()
print(multiplier(10, 11))
print(multiplier.__name__)

def get_multiplier2(number):
    def inner2(a):
        return a * number
    return inner2

multiplier_by_2 = get_multiplier2(3)
print(multiplier_by_2(11))
print(multiplier_by_2.__name__)

def squarify(a):
    return a**2

a = list(map(squarify, range(5))) # можно tuple, set и другое
print(a)

squared_list = []

for number in range(5):
    squared_list.append(squarify(number))

print(squared_list)

def is_positive(a):
    return a > 0

b = list(filter(is_positive, range(-2, 5)))
print(b)

positive_list = []

for number in range(-2, 5):
    if is_positive(number):
        positive_list.append(number)

print(positive_list)

c = list(map(lambda x: x ** 2, range(8)))
print(c)

print(type(lambda x: x ** 2))

d = list(filter(lambda x: x > 0, range(-2, 5)))
print(d)

e = list(map(lambda x: str(x), range(15))) 
print(e)
#or
def stringify_list(num_list):
    return list(map(str, num_list))

print(stringify_list(range(10)))

def multiply(a, b):
    return a * b

print(reduce(multiply, [1,2,3,4,5]))

print(reduce(lambda x, y: x * y, range(1, 5)))

def greeter(person, greeting):
    return '{}, {}!'.format(greeting, person)

heir = partial(greeter, greeting='Hi')
helloer = partial(greeter, greeting='Hello')

print(heir('bro'))
print(helloer('sir'))

squared_list2 = []

for number in range(10):
    squared_list2.append(number ** 2)

print(squared_list2)

squared_list3 = [number ** 2 for number in range(10)]
print(squared_list3)

even_list = [num for num in range(20) if num % 2 == 0]
print(even_list)

squared_dict = {number: number ** 2 for number in range(6)}
print(squared_dict)

reminders_set = {num % 10 for num in range(100)}
print(reminders_set)

print(type(num ** 2 for num in range(10)))

num_list2 = range(7)
squared_list_zip = [x ** 2 for x in num_list2]

print(list(zip(num_list2, squared_list_zip)))