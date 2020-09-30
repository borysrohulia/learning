from datetime import datetime

def get_seconds():
    """Return current second"""
    return datetime.now().second

print(get_seconds())

print(get_seconds.__doc__)
print(get_seconds.__name__)

def split_tags(tag_string):
    tag_list = []
    for tag in tag_string.split(','):
        tag_list.append(tag.strip())

    return tag_list

print(split_tags('python, coursera, mooc'))

# annotation types in python3

def add(x: int, y: int) -> int:
    return x + y

print(add(10, 11))
print(add('still ', 'works'))

def extender(source_list, extend_list):
    source_list.extend(extend_list)

values = [1,2,3]
extender(values, [4,5,6])

print(values)

def replacer(source_tuple, replace_with):
    source_tuple = replace_with

user_info = ('Guido', '31.01')
replacer(user_info, ('Larry', '27.09'))

print(user_info)

def say(greeting, name):
    print('{} {}!'.format(greeting, name))

say('Hello', 'Borys')
say(name='Borys', greeting='Hello')

# Области видимости

# внизу код не работает из-за области видимости 

# result = 0

# def increment():
#     result += 1
#     return result

# print(increment())

def greeting_func(name='it\'s me...'):
    print('Hello, {}'.format(name))

greeting_func()

#  не правильно передавать изменяемые значения
def append_one(iterable=[]):  
    iterable.append(1)
    return iterable

print(append_one([1]))
print(append_one())
print(append_one())

print(append_one.__defaults__)

#  лучше написать вот так функцию:

def function_right(iterable=None):
    if iterable is None:
        iterable = []

#  или так:

def function_right2(iterable=None):
    iterable = iterable or []

def printer(*args):
    print(type(args))

    for arguments in args:
        print(arguments)

printer(1,2,3,6,8)

name_list = ['John', 'Smith', 'Borys', 'Tania']

printer(*name_list)

def printer2(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print('{}: {}'.format(key, value))

printer2(a=10, b=11)

payload = {
    'user_id': 117,
    'feedback': {
        'subject': 'Registration fields',
        'message': 'There is no country for old man'
    }
}

# printer2(**payload)

def foo(*args, **kwargs):
    print(args)
    print(kwargs)

foo(*name_list, **payload)