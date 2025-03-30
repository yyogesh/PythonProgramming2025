l1 = [1, 2, 3, 4, 5]
L2 = ['a', 'b', 'c', 'd', 'e', 'f']

d1 = dict(zip(l1, L2))
print(d1)

print({x:y for x, y in zip(l1, L2)})