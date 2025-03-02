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
# find Returns the index of the first occurrence of a substring or -1.
# rfind Returns the index of the last occurrence of a substring or -1.
# index Returns the index of the first occurrence of a substring or raises an exception if not found.
# rindex Returns the index of the last occurrence of a substring or raises an exception if not found.
# count Returns the number of occurrences of a substring.
print(s.find('l'))
print(s.find('l', 6, 11))
print(s.rfind('l', 2, 11))

print(s.index('o'))

print("********************************")

text = "Python is fun. Python is easy."
print(text.count("Python")) #2

print("********************************")
# "    test   "
text = "   Pyt hon   "
print(text.strip())

print("********************************")

text = "Python"
print(text.ljust(10, '*'))

text = "Python"
print(text.rjust(10, '*'))
print(text.center(11, '*'))
print("sec tion".center(50, '*'))


print("********************************")

text = "hello world"
print(text.capitalize())
print(text.title())
print(text.upper())
print(text.lower())


print("********************************")
text = "Hello World"
print(text.swapcase())

print("********************************")
s = 'Bu\u00DF'
s1 = 'Buss'
print(s)
print(s.casefold())
print(s.lower())

print(s == s1)
print(s.casefold() == s1.casefold())

text = "Straße" 
print(text.casefold())


print("********************************")

print(dir(s))


print("********************************")
s = "HELLO"
print(s.islower())
print(s.isupper())
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
print(s.isascii())
print(s.isprintable())

print("HELLO".isupper())
print("hello".islower())
print("123".isdigit())
print("hello123".isalnum())
print("hello".isalpha())
print("hello".isascii())
print("hello".isprintable())

print("********************************")
print("hello123".isalnum())
print("hello".isalnum())
print("123".isalnum())
print("こんにちは".isascii())
print("he\tllo".isprintable())
print(" ".isspace())
print("123".isdecimal())
print("12.3".isdecimal())
print("123".isdigit())
print("123".isnumeric())
print("Ⅷ".isnumeric())
print("hello".isidentifier())
print("hello_abc".isidentifier())
print("123hello_abc".isidentifier())
print("length-1".isidentifier())
print("while".isidentifier())


print("********************************")
s ="python is very easy"
print(s.startswith("python"))

print(s.startswith("is", 7))

email = "yogesh@gmail.com" #find
print(email.find("@"))
print(email.startswith("gmail", email.find("@") + 1))

print(email.endswith("gmail.com"))

print("********************************")
text = "Hello, world!"
result = text.removeprefix("1Hello, ")
print(result)
print(text.removesuffix("world!"))

print("********************************")
text = "Hello, world!"
result = text.partition("o")
print(result)

print("********************************")
s = "999-999-9999-8474"
print(s.replace("-", " "))
print(s.replace("-", "$", 2))

print("********************************")
s = '99-99---99---999'
print(s.replace("-", " "))

print("********************************")
s = "abcd"
a = "1234"
print(s.join(a))
print('/'.join(a))
list = ["apple", "banana", "cherry"]
print(" and ".join(list))

print("********************************")
s = "abc xyz pqr"
print(s.split())

s = "abc,xyz,pqr"
print(s.split(','))

s = "abc,xyz,pqr,ghr,kuy"
print(s.split(',',2))

s = "abc,xyz,pqr,ghr,kuy"
print(s.rsplit(',',2))