l1 = []

for i in range(10):
    l1.append(i) # append only one element extend can add list

print(l1)

x = 10
result = "Even" if x %2 == 0 else "Odd"
print(result)

x = 15
print("Divisible by 5" if x % 5 == 0 else "Not divisible by 5")

print("Postive and Even" if x > 0 and x %2 == 0 else "Positive and odd" if x > 0 else "Negative or Zero")

print([x**2 for x in range(10)])

print([x for x in range(10)])

print([x for x in range(10) if x % 2 == 0])

print([x.lower() for x in "WelCoMe"])

numbers = [1, 2, 3, 4, 5]
print(["Even" if x % 2 == 0 else "Odd" for x in numbers])