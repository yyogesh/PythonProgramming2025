numbers = [5, 2, 9, 1]
print(sorted(numbers))

words = ["apple", "banana", "cherry", "date"]
print(sorted(words, key=len))  # Sort by length

print(sorted(numbers, reverse=True))

numbers = [1, 2, 3, 4]
print(list(reversed(numbers)))


def is_palindrome(word):
    return word == ''.join(reversed(word))
print(is_palindrome("madam")) 

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
s = slice(2, 8, 2)  # start stop step
print(numbers[s])
print(numbers[2:8:2]) 

