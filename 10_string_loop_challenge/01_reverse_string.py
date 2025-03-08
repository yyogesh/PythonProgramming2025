print("Hello"[::-1])

s = "Hello"
rs = ''
for char in s:
    print(char)
    rs =  char + rs
print(rs)


# print("********************************")

s = "Hello"
rs = ''.join(reversed(s))
print(rs)

# print("********************************")

s = "Hello"
rs = []
for char in s:
    rs.insert(0, char)
print(''.join(rs))