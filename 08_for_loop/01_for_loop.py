# for(int i = 0; i < 5; i++) {
#     // do something
# }


for i in range(1, 11):
    print("Hello ", i)

print("\n================================")

for i in range(1, 11, 2):
    print("Hello ", i)


print("\n================================")

for i in range(10, 0, -1):
    print("Hello ", i)

print("\n================================")

for i in range(5):
    if i == 3:
        break
    print(i)


print("\n================================")

for i in range(5):
    if i == 3:
        continue
    print(i)


print("\n================================")

for i in range(3):
    print(i)
else:
    print("Loop finished!")


print("\n================================")

for i in range(3):
    if i == 1:
        pass  # Do nothing
    print(i)


print("\n================================")

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i * j}")
    print("------")

