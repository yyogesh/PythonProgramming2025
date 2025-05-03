# Read entire file
with open('example.txt', 'r') as file:
    content = file.read()
    print("Full content:\n", content)


# Read line by line
with open('example.txt', 'r') as file:
    print("Line by line:")
    for line in file:
        print(line.strip())  # strip() removes leading/trailing whitespace


# Read line by line
with open('example.txt', 'r') as file:
    print("Line by line:")
    lines = file.readlines()
    for line in lines:
        print(line.strip())


# Read specific number of characters
with open('example.txt', 'r') as file:
    chunk = file.read(10)  # reads first 10 characters
    print("\nFirst 10 chars:", chunk)



with open('example.txt', 'r+') as file:
    # Get current position
    print("Initial position:", file.tell())

      # Read first 5 characters
    print("First 5 chars:", file.read(5))
    print("Position after read:", file.tell())

    # Move to beginning
    file.seek(0)
    print("Position after seek(0):", file.tell())

     # Move to 10th byte
    file.seek(10)
    print("Position after seek(10):", file.tell())