# for number of times
# as long as the connection is true


count = 0 #1
while count < 10: #2
    print("Hello ", count + 1)
    count += 1 #3


# n = int(input("Enter a number: "))

# while n > 0:
#     print(n)
#     n -= 1


# n = int(input("Enter a number: ")) #98765

# while n > 0:
#     print("n % 10", n % 10) # 5 6 7 8 9
#     print("n // 10", n // 10) # 9876 987 98 9
#     n = n // 10


n = int(input("Enter a number: ")) #98765

while n > 0:
    print("n % 10", n % 10) # 5 6 7 8 9
    # print("n // 10", n // 10) # 9876 987 98 9
    n = n // 10


n = 6
count = 1
while count <= 10:
    print(n, 'x', count, '=', n * count)
    count += 1


n = int(input("Enter a number: ")) #98765

count = 0
while n > 0:
    count += 1
    n = n // 10

print("Number of digits: ", count)