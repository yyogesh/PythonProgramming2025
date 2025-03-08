vowels = "aeiouAEIOU"
s = "hello"
count = 0
for char in s:
    if char in vowels:
        count += 1

print(count)


result = ""
for char in s:
    if char not in vowels:
        result += char

print(result)