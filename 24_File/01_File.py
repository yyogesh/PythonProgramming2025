file = open('example.txt', 'a') 
file.write("Hello, World!")
file.close()
# print(dir(file)) # write mode

file = open('example.txt', 'r') 
content = file.read()
print(content)
file.close()