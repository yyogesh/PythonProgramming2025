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

print("*" * 50)

x1 = [1, 2, 3, 4, 5, 6, 7, 8]
x2 = x1.copy()
print(x1)
print(x2)
print(id(x1), id(x2))
print(id(x1[0]), id(x2[0]))

print("*" * 50)
x1 = [1, 2, 3, 4, 5, 6, 7, 8]
x1.pop()
print(x1)
x1.pop(3)
print(x1)

print("*" * 50)

del x1[2]
print(x1)

del x1[0:2]
print(x1)


print("*" * 50)

x1 = ["a", "b", "c", "d", "e", "f", "g", "h"]
x1.remove('e')
print(x1)

print("*" * 50)

x1 = [1, 2, 3, 4, 5, 6, 7, 8]
x1.clear()
print(x1)

print("*" * 50)
x1 = [1, 2, 3, 4, 5, 6, 7, 8]
del x1[:]
print(x1)

print("*" * 50)
x1 = [1, 2, 3, 4, 5, 6, 7, 8]
x1[:] = []
print(x1)



print("*" * 50)

x1 = ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'd', 'e']
print(x1.index('c'))
print(x1.index('c', 3))
# print(x1.index('z'))

print("*" * 50)

print(x1.count('a'))
print(x1.count('z'))

print("*" * 50)
x2 = ['aa', 'bb', 'cc', 'dd', 'AAA', 'BBB', 'CCC', 'DDD']
print(x2.reverse())
print(x2)

print("*" * 50)

x2.sort()
print(x2)
print(ord('A'))
print(ord('a'))

print("*" * 50)

x2.sort(key=str.lower)
print(x2)

x2.sort(key=str.lower, reverse=True)
print(x2)

print("*" * 50)
x2 = ['aa', 'bb', 'cc', 'dd', 'AAA', 'BBB', 'CCC', 'DDD']
print(sorted(x2))
print(x2)