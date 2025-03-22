t1 = ('ABC', 45, 48.5, False, 'A')

print(t1)
print(t1[0])
print(t1[2])

# immutable

# t1[2] = 50.5
# t1.append(50.5)
print('********************************')
t2 = ()
print(type(t2))

# t3 = (10)
# print(type(t3))

t3 = (10,)
print(type(t3))

t4 = tuple((1, 2, 3, 4))
print(t4)

t5 = tuple('Python')
print(t5)

t6 = ((1, 2), (3, 4), ('a', 'b'))
print(t6[1][1])


t7 = (10, 20, 30, 40, 50)
print(t7)

t8 = 10, 20, 30, 40, # packing
print(t8)

a, b, c, d = t8
print(a, b, c, d)

a, b, c = 'ABC' # unpacking
print(a, b, c)

a, b, c = [1, 2, 3] # unpacking
print(a, b, c)

t9 = (10, 20, 30, 40, 50)
print(t9)

# a, b, c = t9
# print(a, b, c)

# let arr = [10, 20, 30, 40, 50]
# let [a, b, ...d] = arr

a, *b, d = t9
print(a, b, d)


t10 = (10, 20, 30, 40, 50)
for x in t10:
    print(x)

for x in range(len(t10)):
    print(t10[x])

print('********************************')

t11 = (10, 20, 30, 40, 50)
print(t11)
print(t11[0])
print(t11[-1])
print(t11[1:4])
print(t11[:3])
print(t11[2:])
print(t11[::2])
print(t11[::-1])

# t11[1:4] = (25, 35, 45)

print('********************************')

t1 = (1, 2, 3)

t2 = (4, 5, 6)

t3 = t1 + t2

print(t3)

print(t1 + tuple('Python'))
print(t1 + tuple([10, 20, 30]))
print(t1 * 3)

print('********************************')
print(3 in t1)
print(4 in t1)

print('********************************')

l1 = [10, 20, 30, 40, 50]
print([x*2 for x in l1])

print('********************************')
t1 = (10, 20, 30, 40, 50)

t2 = tuple(x*2 for x in t1)
print(t2)

print((x*2 for x in t1))

print(*(x*2 for x in t1))

print((*(x*2 for x in t1),))

print((*(x*2 for x in 'python'),))

print("*" * 50)

t1 = (10, 20, 30, 40, 50, 10, 10, 20, 40, 10)
print(t1.count(10))
print(t1.index(20))


# (product_name, price, quantity)
inventory = [
    ("Laptop", 1200, 10),
    ("Mouse", 25, 50),
    ("Keyboard", 50, 30)
]

total = 0
for item in inventory:
    print(f"Product: {item[0]}, Price: {item[1]}, Quantity: {item[2]}")
    total += item[1] * item[2]
    
print(f"Total: {total}")