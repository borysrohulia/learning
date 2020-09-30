empty_set = set()
number_set = {1,2,3,3,4,5}

print(number_set)

print(2 in number_set)

odd_set = set()
even_set = set()

for number in range(10):
    if number % 2:
        odd_set.add(number)
    else:
        even_set.add(number)

print(odd_set)
print(even_set)

union_set = odd_set | even_set
union_set = odd_set.union(even_set)

print(union_set)

intersection_set = odd_set & even_set
intersection_set = odd_set.intersection(even_set)

print(intersection_set)

difference_set = odd_set - even_set
difference_set = odd_set.difference(even_set)

print(difference_set)

symetric_difference_set = odd_set ^ even_set
symetric_difference_set = odd_set.symmetric_difference(even_set)

print(symetric_difference_set)

even_set.remove(2)
print(even_set)

print(even_set.pop())
print(even_set)

frozen = frozenset(['anna', 'elsa', 'kristoff'])
# frozen.add('olaf')                                Нельзя изменить фрозен сет
