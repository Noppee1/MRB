from random import randint, seed

N_CITIES = 20
seed(111)


def generate_data(data_size):
    res = []
    for i in range(data_size):
        res.append((randint(0, N_CITIES - 1), randint(0, N_CITIES - 1)))
    return res


"""
zadanie2:
 Mając dany "rozkład jazdy" (z pliku gen_train_data.py), napisać funkcję która sprawdzi czy można dojechać
 z miasta "a" do miasta "b" (bez przesiadek).
"""

def is_connected(train_data: list[tuple[int,int]], a: int, b: int) -> bool:
    for (src, dest) in train_data:
        if src == a and dest == b:
            return True

if __name__ == '__main__':
    a = int(input('Podaj miasto początkowe: '))
    b = int(input('Podaj miasto docelowe: '))
    train_schedule = generate_data(40)

    if is_connected(train_schedule, a, b):
        print('Istnieje takie połączenie')
    else:
        print('Nie ma takiego połączenia')