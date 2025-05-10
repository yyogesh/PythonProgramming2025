class Car:
    class Engine:  # Inner class
        def start(self):
            return "Engine started"

    def __init__(self):
        self.engine = self.Engine()  # Create inner class instance

car = Car()
print(car.engine.start())  # Output: Engine started