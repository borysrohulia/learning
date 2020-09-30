import random
import statistics

numbers = []

numbers_size = random.randint(10, 15)

for _ in range(numbers_size):
    numbers.append(random.randint(10, 20))

print(numbers)

numbers.sort()

half_size = len(numbers) // 2
mediana = None

if numbers_size % 2 == 1:
    mediana = numbers[half_size]
else:
    mediana = sum(numbers[half_size-1:half_size+1]) / 2



print(statistics.median(numbers))

print(numbers)
print(mediana)