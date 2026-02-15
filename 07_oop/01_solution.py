# 1. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car:
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel

# the class is made as a seperate file.It works as a blank form. Whenever we have to use it we will change the variable part in the below code snippet

#remember the __init__ function & 'self' reference

my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata", "Safari")
print(my_new_car.model)