# \n \r \t \b \f

print("Hello\nWorld", end='')
print("World")

print("abc\fxyz")

# abc
#    xyz

# Moves the cursor to the beginning of the line.
print("Hellooasdfas\rWorld")

print("Hello\bWorld")

print("Hello\tWorld")

print("She said, \"Hello!\"")

print("\x48\x65\x6c\x6c\x6f")

# Raw string
print("Hello\nWorld")

print(r"rHello\nWorld")

# abc@@gmail.com

print("Name:\tJohn\nAge:\t25\nAddress:\t123\\Main St.")

print('\N{pound sign}')

print('\N{rupee sign}')

print('\N{yen sign}')

print('\N{YEN sign}')

print('\N{dollar sign}')

print('\N{copyright sign}')

print('\N{latin small letter a}')

print('\N{superscript five}')

print('\N{subscript five}')

print('\N{black heart suit}')


a = 10
b = "abc"
c = 76.444

print(a, end='\t')
print(b, end='\t')
print(c)

print(a, b, c, sep='-')

#print(a, b, c, file=open('output.txt', 'w'))

# sys.stdout

print("Student name is %s and age is %d and avarge is %f" %(b, a, c))

print('Student name is %10s' % b)

print('Student name is %-10s' % b)

print('Student name is %2.5f' % c)

print("Student name is {0} and age is {0} and avarge is {0}".format(a, b, c))

print("Student name is {} and age is {} and avarge is {}".format(a, b, c))

print("Student name is {0:10} and age is {1:10} and avarge is {2:2.5}".format(a, b, c))

print("Student name is {0:<10} and age is {1:^10} and avarge is {2:2.5F}".format(a, b, c))

print("Student name is {0:<10} and age is {1:^10} and avarge is {2:E}".format(a, b, c))

print(f"Student name is {a} and age is {b} and avarge is {c}")

print(f"Student name is {a:10} and age is {b:^15} and avarge is {c:2.5f}")


