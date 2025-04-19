def double(x):
    return x * 2


x = lambda x: x * 2

print(double(5))  # Call double function with argument 5
print(x(5))  # Call lambda function with argument 5

print((lambda x: x * 2)(5))  # Call lambda function with argument 5


l1 = [1, 2, 3, 4, 5]

f = filter(lambda x: x % 2 == 0, l1)  # Filter even numbers from the list
print(list(f))  # Convert filter object to list and print it



numbers = [1, 2, 3, 4, 5]
# Map
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

names = ["Alice", "Bob", "Charlie", "David"]

print(sorted(names))  # Sort names in ascending order

print(sorted(names, key=lambda x: len(x)))  # Sort names by length


def make_incrementor(n):
    return lambda x: x + n

add5 = make_incrementor(5)
print(add5(10))  # Output: 15