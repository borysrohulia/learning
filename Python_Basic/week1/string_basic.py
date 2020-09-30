# name = input('Input your name: ')
# print(f"Hello {name}!")

a = b"Hello"
print(type(a))

b = "Привет"

c = b.encode(encoding="utf-8")
print(c)

d = c.decode()
print(d)

for letter in b:
    print(letter)

