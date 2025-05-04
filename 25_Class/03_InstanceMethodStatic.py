class Car:
   def add(self, x, y):
      return x + y
   def subtract(self, x, y):
      return x - y
   
   @staticmethod
   def multiply(x, y):
      return x * y
   

print(Car.multiply(2, 3)) # Output: 6
print(Car().add(2, 3)) # Output: 5

