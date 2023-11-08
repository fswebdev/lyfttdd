from abc import ABC, abstractmethod


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class CarriganTire(Serviceable):

    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        for wear_value in self.tire_wear_array:
            if wear_value >= 0.9:
                return True
        return False


class OctoprimeTire(Serviceable):

    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        wear_sum = sum(self.tire_wear_array)
        return wear_sum >= 3


class Car(Serviceable):

    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self):
        if self.engine.needs_service():
            return True
        if self.battery.needs_service():
            return True

        for tire in self.tires:
            if tire.needs_service():
                return True

        return False
