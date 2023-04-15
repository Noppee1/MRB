from random import randint, seed

N_CITIES = 20
seed(111)


def generate_data(data_size):
    res = []
    for i in range(data_size):
        res.append((randint(0, N_CITIES - 1), randint(0, N_CITIES - 1)))
    return res

"""
zadanie3:
 Mając dany "rozkład jazdy" (z pliku gen_train_data.py), napisać funkcję która sprawdzi czy można dojechać
 z miasta "a" do miasta "b" z dokładnie jedną przesiadką, czyli czy istnieje para połączeń typu (a,c),(c,b).
"""

def is_connected_with_stopover(train_data: list[tuple[int, int]], a: int, b: int) -> bool:
    start = []
    destination = []
    for each in train_data:
        if each[0] == a:
            start.append(each)
        if each[1] == b:
            destination.append(each)

    for out in range(len(start)):
        for in1 in range(len(destination)):
            if start[out][1] == destination[in1][0]:
                return True

if __name__ == '__main__':
    a = int(input('Podaj miasto początkowe: '))
    b = int(input('Podaj miasto docelowe: '))
    train_schedule = generate_data(40)
    print(train_schedule)

    if is_connected_with_stopover(train_schedule, a, b):
        print('Istnieje takie połączenie')
    else:
        print('Nie ma takiego połączenia')