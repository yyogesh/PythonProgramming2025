print("Hello")

print(print.__doc__)
print(print.__name__)
print(print.__module__)


def greet(name):
    return f"Hello, {name}!"

hello = greet
print(hello("Alice"))

functions = [greet, str.upper, len]
print(functions[0]("Bob"))  # Calls greet function
print(functions[1]("hello"))  # Calls str.upper function
print(functions[2]("hello"))  # Calls len function

def apply(func, value):
    return func(value)

print(apply(greet, "hello"))


def outer():
    def inner():
        print("Inner function called")
    inner()  # Call inner function

outer()  # Call outer function


def totalArea(l, b, h):
    def area(length, breadth):
        return length * breadth
    return 2 * (area(l, b) + area(l, h) + area(b, h))


print(totalArea(2, 3, 4))  # Call totalArea function with length, breadth, and height
print(totalArea(5, 6, 7))  # Call totalArea function with different values


def apply_operation(numbers, operation):
    return [operation(num) for num in numbers]

def square(x):
    return x * x

def double(x):
    return x * 2

numbers = [1, 2, 3, 4]

print(apply_operation(numbers, square))  # Call apply_operation with square function
print(apply_operation(numbers, double))  # Call apply_operation with double function



def create_greeting(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet

say_hello = create_greeting("Hello")
say_hi = create_greeting("Hi")

print(say_hello("Alice"))  # Output: Hello, Alice!
print(say_hi("Bob"))      # Output: Hi, Bob!


def counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

counter1 = counter()
print(counter1())  # Output: 1
print(counter1())  # Output: 2
print(counter1())  # Output: 3