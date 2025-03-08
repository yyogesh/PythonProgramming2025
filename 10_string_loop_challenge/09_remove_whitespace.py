def remove_whiltespace(s):
    result = ""
    for char in s:
        if char != " ":
            result += char
    return result
    #return "".join(s.split())


print(remove_whiltespace("Hello World"))  # HelloWorld