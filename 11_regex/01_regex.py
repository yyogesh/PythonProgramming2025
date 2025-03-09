from re import *

print(match('a', 'a').group())
print(match('a|b', 'a').group()) # either a or b
print(match('a|b', 'b').group()) # extracting specific parts of the matched string

# . * + ? {} [] () ^ $ | \ -

print(match('[abc]', 'ab').group()) # either a b and c
print(match('[abc]+', 'abded').group())
print(match('[abc]+', 'ccccc').group()) # + one or more repetitions
print(match('[abc]+', 'ababdbdceagh').group())
print(match('[abc]{5}', 'abcabcabc').group()) # {4} exactly 4 repetitions
print(match('[abc]{3,5}', 'abcaaed').group()) # {3,5} between 3 and 5 repetitions


print(match('[a-z]', 'ab').group())
print(match('[a-z]+', 'ab').group())
print(match('[a-zA-Z0-9]+', 'abC123').group())
print(match('[a-zA-Z0-9]+', 'ab$$$123').group())
print(match('[^a-z]+', 'AB12a').group()) # matchs characters that are not in the set

print(match('[a-z]+[A-Z]', 'abcCD').group())
print(match('[a-z]+[A-Z]+', 'abcCD').group())
print(match('[a-z]+|[A-Z]+', 'abcCD').group())

print(match('([a-z]+)|([A-Z]+)', 'abcCD').group())

print(match('.+', 'abc').group()) # . any character except newline
print(match('.+', 'abc\nxyz').group())


print(match('a*', 'abc').group()) # * zero or more repetitionsld
print(match('^all', 'allabc').group()) # ^ start of the string

# print(match('world$', 'hello world').group()) # $ end of the string

# print(match('\d', 'abc123').group())
print(match('\d', '1123123').group())
print(match('\d+', '12344').group())

print(match('\D+', 'abc').group())
print(match('\s', ' abc ').group())
print(match('\S+', 'abc').group())
print(match('\w', 'abc').group())
print(match('\W+', '$$$').group())

# print(match('a(?=b)', 'abc').group()) # positive lookahead

text = "The price is $123.453434."
#pattern = '\d+\.\d+'
pattern = r'\d+\.\d{2}'
match = search(pattern, text)
if match:
    print("Found: ", match.group())


text = "John: 30, Jane: 25"
pattern = r'(\w+): (\d+)'
match = search(pattern, text)
if match:
    print("Found: ", match.group())
    print("Name: ", match.group(1))
    print("Age: ", match.group(2))

text = "John: 30, Jane: 25"
pattern = r'(\w+): (\d+)'
matches = finditer(pattern, text)

for match in matches:
    print(f"Name: {match.group(1)}, Age: {match.group(2)}")



text = "Contact us at support@example.com or sales@example.org"
# pattern = r'[\w\.-]+@[\w\.-]+'
pattern = r'[\w\.-]+@[\w\.-]+' # email
matchs = findall(pattern, text)
print(matchs)


text = "Colors: #FFFFFF, #fff, #123abc, #456."
pattern = r'#([A-Fa-f0-9]{6})'
matchs = findall(pattern, text)
print(matchs)

# 192.168.0.1
text = "IP addresses: 237.84.2.178, 244.178.44.111, 244.178.44.111."
pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
matchs = findall(pattern, text)
print(matchs)


text = """Start
This is a multi-line text.
End"""
pattern = r'Start.*End' # match any character
match = search(pattern, text, DOTALL)
if match:
    print("Found: ", match.group())