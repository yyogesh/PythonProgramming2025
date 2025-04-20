print("Hello world")
      
print(10 / 0)

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


try:
    d = {'a': 1}
    print(d['b'])
except KeyError:
    print("Key not found in dictionary!")


try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Index out of range!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")



try:
    # Code that might raise different exceptions
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result is:", result)
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")



try:
    print("Trying to divide...")
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero!")
else:
    print("Division successful! Result is:", result)


try:
    f = open("file.txt", "r")
    data = f.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("This always runs")
    f.close()  # Ensure the file is closed even if an error occurs



class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass

def square_root(x):
    if x < 0:
        raise NegativeNumberError("Cannot compute square root of negative number")
    return x ** 0.5

try:
    result = square_root(-4)
except NegativeNumberError as e:
    print(e)



try:
    try:
        num = int(input("Enter a number: "))
        result = 100 / num
    except ValueError:
        print("Invalid number entered")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print("Result is:", result)

except Exception as e:
    print(f"An unexpected error occurred: {e}")
