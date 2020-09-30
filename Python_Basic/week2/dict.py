from collections import OrderedDict

empty_dict = {}
empty_dict = dict()

collections_map = {
    'mutable': ['list', 'dict', 'set'],
    'immutable': ['tuple', 'frozenset']
}

print(collections_map['immutable'])
print(collections_map.get('irresitable', 'not found'))

print('mutable' in collections_map)

beatles_map = {
    'Paul': 'Bass',
    'John': 'Guitar',
    'George': 'Guitar'
}

print(beatles_map)

beatles_map['Ringo'] = 'Drums'

print(beatles_map)

del beatles_map['John']

print(beatles_map)

beatles_map.update({
    'John': 'Guitar'
})

print(beatles_map)

print(beatles_map.pop('Ringo'))

print(beatles_map)

unknown_dict = {}

print(unknown_dict.setdefault('key', 'default'))
print(unknown_dict)
print(unknown_dict.setdefault('key', 'new_default'))

print(collections_map)

for key in collections_map:
    print(key)

for key, value in collections_map.items():
    print('{} - {}'.format(key, value))

for value in collections_map.values():
    print(value)

for key in collections_map.keys():
    print(key)

ordered = OrderedDict()

for number in range(10):
    ordered[number] = str(number)

for key in ordered:
    print(key)