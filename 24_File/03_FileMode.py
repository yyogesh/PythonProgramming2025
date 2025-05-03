# Write mode (overwrites existing file)
with open('example.txt', 'w') as file:
    file.write("This will overwrite the entire file.\n")


# Append mode (adds to existing file)
with open('example.txt', 'a') as file:
    file.write("This will append to the file.\n")


# Read mode
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)


# Read mode
with open('example.txt', 'r') as file:
    content = file.readlines()
    print(content)


# Read and write mode
with open('example.txt', 'r+') as file:
    content = file.read()
    file.write("\nAdded with r+ mode")


# Binary mode for non-text files
with open('image.jpg', 'rb') as file:
    data = file.read()

# Write binary mode
with open('copy.jpg', 'wb') as file:
    file.write(data)