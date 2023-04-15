a = [2,5,7,9]
b = [4,8,18,27]
wynik = []

for ax in range(len(a)):
    count = 0
    for i in range(len(b)):
        if b[i] % a[ax] == 0:
            count += 1
    wynik.append(count)

print(wynik)