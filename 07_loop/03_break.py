count = 0
 
while count < 10:
    count += 1
    print("Hello ", count)
    if count >= 5:
        break


count = 0
while count < 10:
    n = int(input("Enter a number: ")) #4
    if n % 3 == 0:
        continue
    print(n)
    count += 1
    

