# old methods

# class Pet:
#     pass

# class Dog(Pet):
#     pass

# class ExportJSON:
#     def to_json(self):
#         pass

# # class ExDog(Dog, ExportJSON):
# #     pass

# class ExportXML:
#     def to_xml(self):
#         pass

# class ExDog(Dog, ExportJSON, ExportXML):
#     pass

# dog = ExDog("Foks", "Mops")
# dog.to_xml()
# dog.to_json()

#  new methods composition
import json

class Pet:
    def __init__(self, name=None):
        self.name = name

class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        # super(ExDog, self).__init__(name)
        self.breed = breed
    
    def say(self):
        return "{0}: waw".format(self.name)

class PetExport:
    def export(self, dog):
        raise NotImplementedError

class ExportJSON(PetExport):
    def export(self, dog):
        return json.dumps({
            "name": dog.name,
            "breed": dog.breed
        })

class ExportXML(PetExport):
    def export(self, dog):
        return """
            <?xml version="1.0" encoding="utf-8"?>
            <dog>
                <name>{0}</name>
                <breed>{1}</breed>
            </dog>
        """.format(dog.name, dog.breed)

class ExDog(Dog):
    def __init__(self, name, breed, exporter=None):
        super().__init__(name, breed)
        self._exporter = exporter or ExportJSON()
        if not isinstance(self._exporter, PetExport):
            raise ValueError("bad exporter", exporter)

    def export(self):
        return self._exporter.export(self)

dog = ExDog("Sharik", breed="Dvorniaga", exporter=ExportXML())
dog2 = ExDog("Tuzik", breed="Buldog", exporter=ExportJSON())
print(dog.export())
print(dog2.export())