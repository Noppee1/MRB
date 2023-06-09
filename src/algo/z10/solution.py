"""""
Zadania na dziś (wieczorem.... /sad)
Dany będzie napis składający się ze znaków < oraz >
np s=<>>>><><>
🇦 Znaleźć długość najdłuższego kawałka składającego się z takich samych znaków; np. <<> -> 2; <> -> 1, <>>><< -> 3
🇧 Znaleźć (jakąś) tablicę liczb całkowitych a kompatybilną z napisem s w tym sensie, że tablica s opisuje relacje między kolejnymi elementami tablicy a
przykład
s = <<>
możliwe rozwiązanie a=[2,8,10,7]
albo a=[4,5,9,-1]
----
przykład 2
s = <><>
możliwe rozwiązanie
a=[2,10,5,8,3]
----
rozwiązania plz na branchach wychodzących z
"""""

def zadanie_a(znaki):

    listaznakow = []
    idx = 1
    wynik = 0
    for znak in znaki:
        listaznakow.append(znak)

    for i in range(0, len(listaznakow)-1):
        if listaznakow[i] == listaznakow[i+1]:
            idx += 1
        else:
            if wynik < idx:
                wynik = idx
            idx = 1

    return wynik

