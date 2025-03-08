def count_works(s):
    count = 0
    in_word = False
    for char in s:
        if char != ' ' and not in_word:
            count += 1
            in_word = True
        elif char == ' ':
            in_word = False

    return count


print(count_works("hello")) # 1
print(count_works("hello world")) # 2