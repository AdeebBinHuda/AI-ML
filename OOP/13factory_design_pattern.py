class Car:
    def drive(self):
        return "driving a car"

class Bike:
    def drive(self):
        return "driving a bike"

class VehicleFactory:
    @staticmethod
    def get_vehicles(type):
        if type == "car":
            return Car()
        elif type == "bike":
            return Bike()
        else:
            return ValueError("Unknown bike")

vehicle= VehicleFactory.get_vehicles("car")
print(vehicle.drive())
