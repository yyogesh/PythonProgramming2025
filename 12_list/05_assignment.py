# 3 ['***', '***', '***']

n = 5

list = []
for i in range(n):
    list.append("*" * n)
print(list)


print(["*" * n for i in range(n)])

hours = [int(x) for x in input("Enter hour per day in a week, seperated by spaces").split()]
per_hour_Amount = int(input("Per hour amount: "))
total = sum(hours)
print(hours, total)
print(per_hour_Amount * total)