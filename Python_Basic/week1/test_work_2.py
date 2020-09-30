import sys

digit_string = sys.argv[1]
digit = int(digit_string)
# string_var = ' ' * digit

# for i in range(len(string_var)):
#     lst = list(string_var)
#     lst[i] = '#'
#     string_var = ''.join(lst)
#     print(string_var[::-1])

for i in range(1, digit+1):
    s = i*"#" + (digit + 1 - i)*' '
    print(s[::-1])