def longest_word(s):
    words = s.split() #list split by space
    longest = ""
    for word in words:
        print(len(word), len(longest))
        if len(word) > len(longest):
            longest = word
    return longest


print(longest_word("Hello1 World welcome to the Python")) # welcome