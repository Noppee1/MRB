import matplotlib.pyplot as plt

dane = [
    5, 0.7,
    10, 0.75,
    100, 2.4,
    200, 4.9,
    400, 11,
    800, 29,
    1600, 86,
    3200, 224,
    6400, 497,
    12800, 1092]



x, y = [1], [1]

for i in dane:
    if i % 2 == 0:
        x.append(i)
    else:
        y.append(i)

print(x)
print(y)

x, y = dane[::2], dane[1::2]

plt.plot(x, y)
plt.xlabel('rozmiar')
plt.ylabel('czas')
plt.show()