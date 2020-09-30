company = 'my.comp'

if 'my' in company:
    print('this is my company')


company2 = 'test.net'

if 'my' in company2 or company2.endswith('.net'):
    print('Yes')

company3 = 'google.com'

if 'my' in company3:
    print('Aliluya')
else:
    print('toge aliluya')

company4 = 'google.com'

if 'my' in company4:
    print('Aliluya')
elif 'google' in company4:
    print('srabotal elif')
else:
    print('toge aliluya')

score_1 = 5
score_2 = 0

winner = 'Argentina' if score_1 > score_2 else 'Jamaica'
print(winner)

i = 0

while i < 100:
    i += 1

print(i)

name = 'Alex'

for letter in name:
    print(letter)

for i in range(3):
    print(i)

result = 0

for i in range(101):
    result += i

print('Result: ', result)

for i in range(5, 8):
    print(i)

for i in range(1, 10, 2):
    print(i)

for o in range(10, 1, -1):
    print(o)

for t in range(100):
    pass


result2 = 0
while True:
    result2 += 1
    if result2 >= 100:
        break 

print('result2: ', result2)

for i in range(10):
    if i == 5:
        break
    print('i: ', i)

result3 = 0

for i in range(10):
    if i % 2 != 0:
        continue
    result3 += i
print(result3)