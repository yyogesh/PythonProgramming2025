result = ""
s = set()
s1 = "hello"
for char in s1:
    if char not in s:
        result += char
        s.add(char)

print(result)