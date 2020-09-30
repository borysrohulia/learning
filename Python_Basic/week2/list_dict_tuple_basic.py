import random

empty_list = []
empty_list = list()

none_list = [None] * 10

collections = ['list', 'tuple', 'dist', 'set']

user_data = [
    ['Elena', 4.4],
    ['Andrey', 4.2]
]

len(collections)

print(collections)
print(collections[0])
print(collections[-1])

collections[3] = 'fozenset'

print(collections)

print('tuple' in collections)

range_list = list(range(10))
print(range_list)

print(range_list[1:3])
print(range_list[3:])
print(range_list[:5])
print(range_list[::2])
print(range_list[::-1])
print(range_list[1::2])
print(range_list[5:1:-1])

print(range_list[:] is range_list)

for collection in collections:
    print('Learning {}...'.format(collection))

for idx, collection in enumerate(collections):
    print('#{} {}'.format(idx+1, collection))

collections.append('OrderDict')
print(collections)

collections.extend(['borys', 'tanya'])

print(collections)

collections += [None]
print(collections)

del collections[4]

print(collections)

numbers = [10, 4, 89, 45, 101, 123, 7, 56, 43]

print(min(numbers))
print(max(numbers))
print(sum(numbers))

tag_list = ['python', 'course', 'coursera']
print(', '.join(tag_list))

numbers = []

for _ in range(10):
    numbers.append(random.randint(1, 20))

print(numbers)

print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(numbers)

numbers.sort()
numbers.sort(reverse=True)
print(numbers)

print(reversed(numbers))

empty_tuple = ()
empty_tuple = tuple()

immutables = (int, str, tuple)

# immutables[0] = float                         - Нельзя менять tuple!!!!!

blink = ([], [])
blink[0].append(0)

print(blink)

print(hash(tuple()))

#  один елемент  надо поставить запятую в конце!!!! смотри вниз

one_element_tuple = (1, )       