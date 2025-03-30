d1 = {1: 'ONE', 2: 'TWO', 3: 'THREE'}

print(d1.keys())
print(d1.values())
print(d1.items())

for x in d1.keys():
    print(x)

for x in d1.values():
    print(x)

for x, y in d1.items():
    print(x, y)


print(d1[2])
print(d1.get(2))

# print(d1[5])
print(d1.get(5, 'Not Found'))

d1.setdefault(4, 'FOUR')
print(d1)


d1.update({5: 'FIVE', 6: 'SIX', 2: 'TWOX'})
print(d1)

l1 = [1, 2, 3, 4]
print(dict.fromkeys(l1))

print(dict.fromkeys(l1, 'Value'))

d2 = d1.copy()
print(d2)

print(id(d1[1]), id(d2[1]))

d1[1] = 'ONEX'
print(id(d1[1]), id(d2[1]))

print(d1, d2)

d1.pop(1)
print(d1)

d1.pop(10, 'Not Found')
print(d1.pop(10, 'Not Found'))

# d1.popitem()

d1.clear()