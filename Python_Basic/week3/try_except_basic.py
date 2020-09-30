# print(1/0)     # - ZeroDivisionError: division by zero



# class MyClass:
#     pass
# obj = MyClass()
# print(obj.foo)    # - AttributeError: 'MyClass' object has no attribute 'foo'



# d = {"foo": 0}
# print(d["bar"])  # - KeyError: 'bar'



# l = [10, 20]
# print(l[10])   #  -   IndexError: list index out of range



try:
    1/0
except Exception:
    print("Error: my error")


# while True:
#     try:
#         raw = input("enter num: ")
#         number = int(raw)
#         break
#     except:
#         print("uncorrection value")

# while True:    # - this right
#     try:
#         raw = input("enter num: ")
#         number = int(raw)
#         break
#     except ValueError:
#         print("uncorrection value")

# while True:
#     try:
#         raw = input("enter num: ")
#         number = int(raw)
#     except ValueError:
#         print("uncorrection value")
#     else:
#         break

# while True:
#     try:
#         raw = input("enter num: ")
#         number = int(raw)
#         break
#     except ValueError:
#         print("uncorrection value")
#     except KeyboardInterrupt:
#         print("exit")
#         break

# while True:
#     try:
#         raw = input("enter num: ")
#         number = int(raw)
#         break
#     except (ValueError, KeyboardInterrupt):
#         print("uncorrection value")
#         break

print(issubclass(KeyError, LookupError))
print(issubclass(IndexError, LookupError))

database = {
    "red": ["fox", "flower"],
    "green": ["peace", "M", "python"]
}

try:
    color = input("enter color: ")
    number = input("enter size: ")

    label = database[color][int(number)]
    print("Your choise: ", label)
except LookupError:
    print("Look not found")


# about finally

f = open("/path")
try:
    for line in f:
        print(line.rstrip("\n"))
        1/0
except OSError:
    print("error!")
finally:
    f.close()