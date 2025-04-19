# def Outer(f):
#     def Inner():
#         print("+" * 15)
#         f()
#         print("+" * 15)
#     return Inner

# def display():
#     print("Welcome to Python")


# display = Outer(display)  # Decorate the display function
# display()  # Call the decorated display function




import time


def Outer(f):
    def Inner():
        print("+" * 15)
        f()
        print("+" * 15)
    return Inner

@Outer
def display():
    print("Welcome to Python")


# display = Outer(display)  # Decorate the display function
display()  # Call the decorated display function




def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")






def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.4f} seconds")
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(1)


slow_function()