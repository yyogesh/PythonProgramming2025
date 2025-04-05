def greet(name, /, greeting="Hello"): #arguments before / must be positional.
    print(f"{greeting}, {name}!")


greet("Alice")  # Uses default greeting
greet("Bob", "Hi")  # Uses custom greeting
# greet(name = "Alice") # invalid, name is positional-only
greet("Alice")

def fun(a, b, /, c, d, e):
    print(a, b, c, d, e)

fun(1, 2, 3, 4, 5)
fun(1, 2, c=3, d=4, e=5) # keyword argument
# fun(a=1, b=2, 3, 4, 5) # invalid, a and b are positional-only

def fun(a, b,  c, d, e, /):
    print(a, b, c, d, e)

fun(1, 2, 3, 4, 5)
# fun(1, 2, c=3, d=4, e=5) # keyword argument invalid

# def fun(/, a, b,  c, d, e):
#     print(a, b, c, d, e)

# fun(1, 2, 3, 4, 5)

def fun(a, b, *, c, d, e):
    print(a, b, c, d, e)

fun(1, 2, c=3, d=4, e=5) # keyword argument
# fun(1, 2, 3, 4, 5) # invalid, c, d, e are keyword-only


def fun(*, a, b,  c, d, e):
    print(a, b, c, d, e)

fun(a=1, b=2, c=3, d=4, e=5) # keyword argument
# fun(1, 2, 3, 4, 5) # invalid, a, b are keyword-only


def func(a, /, b, *, c):
    print(a, b, c)

func(1, b=2, c=3) # valid



def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total


print(sum_all(1, 2, 3))  # Output: 6
print(sum_all(4, 5, 6, 7, 8))  # Output: 30

# print(sum_all(4, 5, 6, 7, c = 8))

# def sum_all1(*args):
#     total = 0
#     for key, value in args.items():
#         print(f"{key}: {value}")
#         total += value
#     # return total

# sum_all1(a=1, b=2, c=3)
# print(result)  # Output: 6

def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")


def get_User():
    name = "John"
    age = 30
    return name, age


user_name, user_age = get_User()
print(user_name, user_age)