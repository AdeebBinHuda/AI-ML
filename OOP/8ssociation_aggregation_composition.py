# association
class Laptop:
    def __init__(self, brand):
        self.brand = brand

class Student:
    def __init__(self, name, laptop_obj):
        self.name = name
        self.laptop_v = laptop_obj

    def show_details(self):
        print(f"Student name: {self.name} has a laptop named {self.laptop_v.brand}")