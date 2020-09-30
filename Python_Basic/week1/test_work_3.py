import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

D = b**2 - 4*a*c

if D > 0:
    x1 = (-b + D**0.5)/2*a
    x2 = (-b - D**0.5)/2*a
    print(x1, '\n', x2)
elif D == 0:
    x1 = -(b/2*a)
    print(x1)
else:
    print('уравнение не имеет корней')