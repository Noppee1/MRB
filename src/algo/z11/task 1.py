import hashlib

from zad_a import *

bag = get_new_bag(100)
def wrzuc(bag: list[list], element: str):
    M = len(bag)
    h = element.__hash__()
    idx = h % M
    bag[idx].append(element)

def zawiera(bag: list[list], element: str):
    M = len(bag)
    h = element.__hash__()
    idx = h % M
    if bag[idx].__contains__("h"):
        print("Zawiera element")
    else:
        print("Nie zawiera elementu")


zawiera(bag, "h")
wrzuc(bag, "h")
zawiera(bag, "h")


# -----------------
# zadanie domowe
# -----------------


str2hash = 'niewiem co pisze'
wynik = hashlib.md5(str2hash.encode())
print(wynik.hexdigest())

result = hashlib.md5(b'niewiem co pisze')
print(result.hexdigest())

