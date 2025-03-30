def getInfo(parameter):
    print(parameter)
    return parameter


getInfo("Hello")
# getInfo(10)
# getInfo(10.5)
# getInfo([1, 2, 3])
# getInfo((1, 2, 3))
# getInfo({1, 2, 3})
# getInfo({"name": "John", "age": 25})

# def getInfo(formal_parameter):
#     print(formal_parameter)
#     return formal_parameter


# getInfo(actual_parameter="Hello")

# if __name__ == "__main__":
#     getInfo(actual_parameter="Hello")


def volume(length, width, height):
    height = 10
    return length * width * height

height = 5
print(volume(1, 2, 5)) # positional argument
print(height)


def volume(length, width, height):
    print(length, width, height)
    return length * width * height

print(volume(height=1, length=2, width=5)) # keyword argument

print("_"* 20)

def volume(length, width, height = 20):
    print(length, width, height)
    return length * width * height

print(volume(1, 2, height=5)) # keyword argument

# print(volume(1, length = 2, height=5)) # keyword argument

# print(volume(length = 1, 2, 5)) # keyword argument

print(volume(1, 2))

l1 = [1, 2, 3, 4, 5]

# l1.index(1, 2)

# l1.index(3, 2, 3)

def fun(a = 1, b = 2.4, c = [1, 2, 3]):
    print(a, b, c)


fun()

fun(5, 10, [10, 11])

print("_"* 20)

def fun(a = 1, b = 2.4, c = [1, 2, 3]):
    c = 20
    print(a, b, c)

fun()
fun(5, 10, [10, 11])


print("_"* 20)

def fun(a = [1, 2, 3]):
    a.append(len(a))
    print(a)

fun()
fun()
fun()
fun([10, 11])
fun()