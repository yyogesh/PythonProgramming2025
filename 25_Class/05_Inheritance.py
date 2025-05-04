class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Animal speaks"
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed

    def speak(self):
        return "Woof!"
    

dog = Dog("Buddy", "Labrador")
print(dog.name, dog.breed)  # Buddy Labrador
print(dog.speak())  # Output: Woof! (method overriding)