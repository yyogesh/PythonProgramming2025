# 7! => 7 *6 *5 *4 *3 *2 *1

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)