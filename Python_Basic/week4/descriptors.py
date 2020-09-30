class Descriptor:
    def __get__(self, obj, type_obj):
        print('get')

    def __set__(self, obj, value):
        print('set')

    def __delete__(self, obj):
        print('delete')

class Class:
    attr = Descriptor()

instance = Class()

instance.attr
instance.attr = 10
del instance.attr


class Value:
    def __init__(self):
        self.value = None

    @staticmethod
    def _prepare_value(value):
        return value*10

    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        self.value = self._prepare_value(value)

class ClassValue:
    attr = Value()


value_instance = ClassValue()
value_instance.attr = 10

print(value_instance.attr)


class ImportantValue:
    def __init__(self, amount):
        self.amount = amount

    def __get__(self, obj, obj_type):
        return self.amount

    def __set__(self, obj, value):
        with open('log.txt', 'w') as f:
            f.write(str(value))
        self.amount = value

class Account:
    amount = ImportantValue(100)

bobs_count = Account()
bobs_count.amount = 40


# какой-то эсперимент

class Test:
    def method(self):
        pass

obj = Test()

print(obj.method)
print(Test.method)

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

petya = User('petya', 'ivanov')
print(petya.full_name)
print(User.full_name)

# создаем свой собственный проперти который копирует поведение встроенного проперти

class Property:
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, obj, obj_type=None):
        if obj is None:
            return self

        return self.getter(obj)


class TestForProperty:
    @property
    def original(self):
        return 'original'

    @Property
    def custom_sugar(self):
        return 'custom_sugar'

    def custom_pure(self):
        return 'custom_pure'

    custom_pure = Property(custom_pure)

obj = TestForProperty()

print(obj.original)
print(obj.custom_sugar)
print(obj.custom_pure)

# делаем статик и класс методы

class StaticMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, obj_type=None):
        return self.func


class ClassMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, obj_type=None):
        if obj_type is None:
            obj_type = type(obj)

        def new_func(*args, **kwargs):
            return self.func(obj_type, *args, **kwargs)

        return new_func

class ForSlots:
    __slots__ = ['my_attr']

    def __init__(self):
        self.my_attr = 'attribute one'

slot_obj = ForSlots()
# slot_obj.second_attr = 'attribute two'        - не можем добавить атрибут
# print(slot_obj.second_attr)