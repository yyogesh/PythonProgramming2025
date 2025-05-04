class Car:
    wheels = 4  # Class variable shared by all instances of the class
    # Constructor method
    def __init__(self, make, model, year):
        self.make = make  # Instance variable for the car's make
        self.model = model  # Instance variable for the car's model
        self.year = year  # Instance variable for the car's year


# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)  # Passing arguments to the constructor
print(my_car.make)  # Output: Toyota
print(my_car.model)  # Output: Corolla  
print(my_car.year)  # Output: 2020
print(my_car.wheels)  # Output: 4 (shared class variable)
print(Car.wheels)  # Output: 4 (accessing class variable directly from the class)