from random import randint

def gen (amount):
    return [randint(1, 100) for _ in range(amount)]

def largest_sum_10_percent() -> int:
    a = gen(100)
    i = 0
    i2 = 10
    wynik = []
    while i2 != len(a):
        wynik.append(sum(a[i:i2]))
        i += 10
        i2 += 10
    return print(max(wynik))


largest_sum_10_percent()