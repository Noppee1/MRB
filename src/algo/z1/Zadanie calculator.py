def add(a, b):
    return a + b


def mul(a, b):
    return a * b


print(add(3, 5),(mul(8, 7)))


def calculate(fn, a, b):
    if fn == add:
        return add(a, b)
    if fn == mul:
        return mul(a, b)


print(calculate(add, 3, 3),calculate(mul, 5, 0))


