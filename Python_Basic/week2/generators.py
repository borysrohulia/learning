def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2

for number in even_range(0, 10):
    print(number)

ranger = even_range(0, 4)

print(next(ranger))
print(next(ranger))

def list_generation(list_obj):
    for item in list_obj:
        yield item
        print('After yielding {}'.format(item))

generator = list_generation([1, 2, 3])

next(generator)
next(generator)
next(generator)

def fibonacci(number):
    a = b = 1
    for _ in range(number):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)

def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got: {}'.format(value))
        if not value: break
        total += value

generator_2 = accumulator()

print(next(generator_2))

print('Accumulated: {}'.format(generator_2.send(1)))
print('Accumulated: {}'.format(generator_2.send(1)))