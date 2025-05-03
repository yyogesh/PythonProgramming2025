with open('example.txt', 'w') as file:
    file.write("Using context manager is safer and cleaner.")


with open('example.txt', 'r') as file:
    print(file.read())