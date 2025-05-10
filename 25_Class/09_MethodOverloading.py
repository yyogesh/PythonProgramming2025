class Calculator:
    def add(self, a, b=None, c=None):
        if b is None and c is None:
            return a
        elif c is None:
            return a + b
        return a + b + c

calc = Calculator()
print(calc.add(1))        # 1
print(calc.add(1, 2))     # 3
print(calc.add(1, 2, 3))  # 6