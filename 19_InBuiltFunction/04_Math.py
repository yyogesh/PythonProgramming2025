import math

print(abs(-10))  # Output: 10

print(abs(-10.5)) 

print(math.sqrt(16))  # Output: 4.0

print(abs(3+4j)) 

print(pow(2, 3))  # Output: 8

print(pow(2, 3, 5))  # Output: 3 (8 % 5)

print(round(4.4))

print(round(4.6))

print(round(4.5))

print(round(5.5)) # banker Rounding

print(round(4.5678, 2))  # Output: 4.57

print(divmod(5, 2))  # Output: (2, 1)

print(min(10, 2, 4, 5, 6))  # Output: 2

print(min([-10, 2, -4, -5, -6], key=abs))  # Output: -2

# print(min([]))  # Output: ValueError: min() arg is an empty sequence

print(min([], default=0))  # Output: 0

print(max(10, 2, 4, 5, 6))  # Output: 10

print(sum([1, 2, 3, 4, 5]))  # Output: 15

print(sum([1, 2, 3, 4, 5], start=10))  # Output: 25

print(eval("print('Hello, World!')"))  # Output: Hello, World!

print(eval("10 * 20 + 30") ) # Output: 230


print(type(10))  # Output: <class 'int'>
print(type(10.5))  # Output: <class 'float'>
print(type("Hello"))  # Output: <class 'str'>
print(type([1, 2, 3]))  # Output: <class 'list'>
print(type((1, 2, 3)))  # Output: <class 'tuple'>
print(type({1: "a", 2: "b", 3: "c"}))  # Output: <class 'dict'>

print(isinstance(10, int))  # Output: True
print(isinstance(10, float))  # Output: False
print(isinstance(10.5, float))  # Output: True

str = "This is a string"
print(hasattr(str, "lower"))  # Output: True
print(hasattr(str, "upper"))  # Output: True
print(hasattr(str, "split"))  # Output: True

print(getattr(math, "pi"))

print(getattr(math, "sqrt"))  # Output: <built-in function sqrt>

print(getattr(math, "sqrt")(25))

l1 = [1, 2, 3, 4, 5]
print(id(l1))  # Output: Memory address of l1
# print(hash(l1))  # Output: TypeError: unhashable type: 'list'

print(dir(list))

print(repr(str)) 