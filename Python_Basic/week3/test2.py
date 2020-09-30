import os

class  CarBase:
    def __init__(self, photo_file_name, brand, carrying):
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]

    
class Car(CarBase):
    def __init__(self, photo_file_name, brand, carrying, passenger_seats_count):
        super().__init__(photo_file_name, brand, carrying)
        self.passenger_seats_count = passenger_seats_count

class SpecMachine (CarBase):
    def __init__(self, photo_file_name, brand, carrying, extra):
        super().__init__(photo_file_name, brand, carrying)
        self.extra = extra


class Truck(CarBase):
    def __init__(self, photo_file_name, brand, carrying, body_whl):
        super().__init__(photo_file_name, brand, carrying)
        self._body_whl = body_whl
        self.list_whl = body_whl.split('x')
        self.valid_whl = len(body_whl.split('x')) == 3

    def body_length(self):
        if self.valid_whl:
            return self.list_whl[0]
        else:
            return 0

    def body_width(self):
        if self.valid_whl:
            return self.list_whl[1]
        else:
            return 0
    
    def body_height(self):
        if self.valid_whl:
            return self.list_whl[2]
        else:
            return 0


kamaz = Truck('kamaz.png','kamaz', 25 ,'45x56x18')
print(kamaz.body_width())