import sys

digit_string = sys.argv[1]

result = 0

for number in digit_string:
    result += int(number)

print(result)