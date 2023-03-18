a = [2, 5, 7, 9]
b = [4, 8, 18, 27]
wynik1 = []
for i in a:
        wynik = 0
        for ix in b:
            if ix % i == 0:
                wynik += 1
        wynik1.append(wynik)
print(wynik1)