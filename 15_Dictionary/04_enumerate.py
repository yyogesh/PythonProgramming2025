l1 = ["One", "Two", "Three", "Four", "Five"]

print(dict(enumerate(l1)))

print(dict(enumerate(l1, start= 100)))

print({x:y for x, y  in enumerate(l1, start= 100)})

print({x: x**2 for x in range(1, 11)})

print({x: x**2 for x in range(1, 11) if x % 2 == 0})