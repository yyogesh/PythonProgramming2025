class Bird:
    def fly(self):
        return "Flying high"

class Penguin(Bird):
    def fly(self):  # Override parent method
        return "Cannot fly"

p = Penguin()
print(p.fly())  # Output: Cannot fly