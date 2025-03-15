list1 = [5, 6, 7, 8, 9, 10, 11, 12]

for i in range(len(list1)):
    print(list1[i])


print("*" * 50)

for item in list1:
    print(item)

print("*" * 50)

for i in range(2, len(list1)):
    print(list1[i])

print("*" * 50)

for item in list1[2:]:
    print(item)


print("*" * 50)

for i in range(len(list1) - 1, -1, -1):
    print(list1[i])


print("*" * 50)

i = 0
while i < len(list1):
    print(list1[i])
    i += 1