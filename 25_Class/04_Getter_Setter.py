class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self): #Getter method
        return (self.celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value): #setter method
        self.celsius = (value - 32) * 5/9


# Example usage
temp = Temperature(25)  # Create a Temperature object with Celsius value of 25
print(temp.fahrenheit)  # Output: 77.0 (Celsius to Fahrenheit conversion)
temp.fahrenheit = 100  # Set Fahrenheit value
print(temp.celsius)  # Output: 37.77777777777778 (Fahrenheit to Celsius conversion)