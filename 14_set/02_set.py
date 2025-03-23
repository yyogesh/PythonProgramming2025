s1 = {10, 20, 30, 40, 50, 60, 70, 80}
for x in s1:
    print(x)

text = "Hello, World!"
s2 = {char.lower() for char in text}
print(s2)


sentence = "The quick brown fox jumps over the lazy dog"
vowels = {char for char in sentence if char.lower() in 'aeiou'}
print(vowels)