def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    # for i in range(2, )

print(is_prime(10)) # False
print(is_prime(11)) # True


# num / 10 # 1234 / 10 = 123
# num // 10 # 1234 % 10 = 4