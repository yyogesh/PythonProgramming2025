class Duck:
    def quack(self):
        return "Quack!"
    
class Person:
    def quack(self):
        return "I can quack like a duck!"
    
def make_quack(obj):
    return obj.quack()
# Create instances of Duck and Person

make_quack(Duck()) 
make_quack(Person())