def count_substring(s, sub):
    count = 0
    print(len(s), len(sub),len(s) - len(sub) + 1)
    for i in range(len(s) - len(sub) + 1):
        print(i, s[i:i+len(sub)])
        if s[i:i+len(sub)] == sub:
            count += 1
    return count

print(count_substring("abababcdab", "abc"))

print("helliiiio".count('i'))
num = "123123123123"
print(len(num) == 10 and num.isdigit())

#leetcode