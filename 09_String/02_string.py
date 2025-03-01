# print("test" * 3)

s = "Hello"
print(type(s))
print(s[0], s[4], s[-1], end=" ** ")
print(s[-5], s[2])
print(len(s))
print(s[0], s[len(s)-1])

print("********************************")
for x in s:
    print(x)

print("********************************")
print('Test')
name = "Alice"
role = "Data Scientist"
experience = 5
profile = f"""
Team Member Profile:
------------------
Name: {name}
Role: {role}
Experience: {experience} years
"""
print(profile)


print("********************************")

s1 = "Hello"
s2 = "Alice"

print(s1 + " " + s2)
#print(15 + 'A')
print(s1 + " " + str(15))

print("*" * 20)
print(20 * "*" )
# print("*" * 2.4)


print("********************************")
s1 = "Hello" #5
for i in range(0, len(s1)):
    print(i, ":", s1[i])

print("********************************")
s1 = "World"
for i in range(len(s1)-1, -1, -1):
    print(i, ":", s1[i])

print("********************************")
s1 = "World"
for i in range(0, len(s1), 2):
    print(i, ":", s1[i])

print("********************************")
# start:end:step
s = "Hello"
print(s[0:2])
print(s[1:4])
print(s[:3])
print(s[3:])
print(s[0: len(s)])
print(s[0: len(s): 1])
print(s[::1])
print(s[::2])
print(s[::-1])
print(s[-1::-1])

print("********************************")
s = "Hello"
print('H' in s)
print('ll' in s)