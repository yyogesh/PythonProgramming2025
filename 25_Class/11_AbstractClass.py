from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Must implement abstract method
        return 3.14 * self.radius ** 2

# shape = Shape()  # Error! Cannot instantiate abstract class
circle = Circle(5)
print(circle.area())  # 78.5