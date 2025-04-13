l1 = [5, 6, 10, 11]
for x in l1:
    print(x)

print("*" * 20)

it = iter(l1)
print(next(it))
print(next(it))
print(next(it))
print(next(it))


# r = range(4)

print("*" * 20)
def my_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

m = my_range(5)
print(next(m))
print(next(m))


