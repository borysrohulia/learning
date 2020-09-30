import functools

def decorator(func):
    return func

@decorator                  #     ==     decorated = decorator(decorated)
def decorated():
    print('Hello')

def my_decorator(func):
    def new_func(*args):
        print(args)
    return new_func()


@my_decorator
def test_func(text):
    print(text)


def logger(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.txt', 'a') as f:
            f.write('\n' + str(result))
        return result
    return wrapped

@logger
def summator(num_list):
    return sum(num_list)

summator([1,2,3,4,5,6,7,8,9,10,11])
print(summator.__name__)

with open('log.txt', 'r') as f:
    print(f.read())

def logger2(filename):
    def log_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'a') as f:
                f.write(str(result))
            return result
        return wrapper
    return log_decorator

@logger2('myfile.txt')
def summator2(num_list):
    return sum(num_list)

summator2([10,20,30,40])

with open('myfile.txt', 'r') as f:
    print(f.read())


def first_decorator(func):
    def wrapped():
        print('From first')
        return func()
    return wrapped

def second_decorator(func):
    def wrapped():
        print('From second')
        return func()
    return wrapped

@first_decorator
@second_decorator
def last_my_decorated_func():
    print('Finaly called...')

last_my_decorated_func()

def bold(func):
    def wrapper():
        return '<b>' + func() + '</b>'
    return wrapper

def italic(func):
    def wrapper():
        return '<i>' + func() + '</i>'
    return wrapper

@bold
@italic
def hello():
    return 'Hello world!'

print(hello())