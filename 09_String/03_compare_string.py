print("hello" == "hello")
print("Hello" == "hello")
print("hello" != "world")
print("apple" < "banana")
print("zebra" > "aardvark")
print("Apple" < "apple") # ASCII a 65 character A is 97

print("Hello".lower() == "hello".lower())
s = "Hello"
# print(dir(s))

# print(help(s.istitle))

print(s.find('e'))
print(s.find('z'))

print("********************************")

s = "Hello, World!"
website = "www.example.com"
# find,rfind
# find(sub, start, end)
# index(sub, start, end
print(s.find('l'))
print(s.find('l', 6, 11))
print(s.rfind('l', 2, 11))

print(s.index('o'))