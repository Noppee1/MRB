
"""
zadanie1:
 Mając dany "rozkład jazdy (z pliku gen_train_data.py), wyświetlić miasto z którego jest najwięcej
 połączeń wychodzących.
"""

from generator import generate_data

def get_city_most_connections(train_data: list[tuple[int,int]]) -> int:
    dictout = {}
    dictin = {}

    for (src, dest) in train_data:
        if src in dictout:
            dictout[src] += 1
        else:
            dictout[src] = 1

        if dest in dictin:
            dictin[dest] += 1
        else:
            dictin[dest] = 1

    print()
    print(dictout)

    maxdictout = max(dictout, key=dictout.get)
    print(f'Miasto z którego dojedziesz do najwiekszej ilości -> {maxdictout}')
    print()
    print(dictin)
    maxdictin = max(dictin, key=dictin.get)
    print(f'Miasto do którego najczesciej dojedziesz -> {maxdictin}')



if __name__ == '__main__':
    rr = generate_data(100)
    print(rr)
    get_city_most_connections(rr)
