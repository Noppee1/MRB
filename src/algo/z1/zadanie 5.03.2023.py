
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def calculate(fn, a, b):
    if fn == 'add':
        return print(add(a, b))
    elif fn == 'mul':
        return print(mul(a, b))


a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
fn = str(input("Co chcesz zrobić? add / mul :  "))

calculate(fn, a, b)