# __init__ dunder method is a constructor, create object
# constructor 3 types
# 1. Default constructor
# 2. Parameterized constructor
# 3. Copy/ Default value constructor
# no return function
"""
# Parameterized constructor
class Car:
    def __init__(self,brand, model, color):
        self.brand=brand
        self.model= model
        self.color= color

car1 = Car("toyota", "corolla", "black")
print(f"Brand: {car1.brand}, Model: {car1.model}, Color: {car1.color}")
"""

# 3   Default value constructor
class Car:
    def __init__(self, brand="toyota", model="corolla", color="black"):
        self.brand=brand
        self.model= model
        self.color= color
car1 = Car()

print(f"Brand: {car1.brand}, Model: {car1.model}, Color: {car1.color}")