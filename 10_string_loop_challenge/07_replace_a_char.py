def replace_char(s, old, new):
    result = ""
    for char in s:
        if char == old:
            result += new
        else:
            result += char
    return result


print(replace_char("hello", "l", "x"))  # hexxo

print("123".isdigit())