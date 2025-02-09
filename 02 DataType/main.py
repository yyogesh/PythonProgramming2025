a = 12
print(a, type(a))
x = 123121234444

print(a.__sizeof__())

print(x.__sizeof__())

a = 12.59
print(a, type(a))

b = 1259E-2
print(b, type(b)) # 1259.0 * 10^-2 = 12.59 
# 1259.0 / 10^2 = 12.59

c = 0.1259E2 # 10 ^ 2 => E2
print(c, type(c))

a = True
print(a, type(a), int(a))

# b= false

# a + ib ==> i ==> 

x = 25 + 3j
print(x, type(x))


y = complex(2.4, 5.9)

print(y, type(y), y.real, y.imag)

a = 1

# a = 12,520

a = 12_520_938_938_938_938_938_938
print(a, type(a))

d = 123_874.45


# decimal = 10
# binary = 2
# octal = 8 0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20
# hexa = 16 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F

a = 20
a = 0b1010
a = 0o15
a = 0x8B

c = 0b101 + 6j

print(c, type(c))


g = int(input("Enter a number: "), 2)
print(g, type(g))

a = 10
print(bin(a))
print(oct(a))
print(hex(a))
print(hex(True))
print(bin(12.5))

# int() # float() # complex() # bool() # str() # list() # tuple() # set() # dict() # frozenset() # bytes() # bytearray() # memoryview() # range() # None


i = "15"
x = float(i)
print(x, type(x))


