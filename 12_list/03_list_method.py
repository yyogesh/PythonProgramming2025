l1 = [4, 5, 6, 7, 8, 9]

# append(x)
# extend(iterable)
# insert(index, x)

l1.insert(2, 100)
print(l1)

print(id(l1))
l1.extend([11, 12, 13])
print(l1)
print(id(l1))

print("*" * 50)
x = 10
print(id(x))
x = 20
print(id(x))
