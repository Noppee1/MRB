from datetime import datetime
import matplotlib.pyplot as plt
from random import seed, randint



def generate_data(datasize):
    # tutaj wstawić coś co generuje dane dla naszego algorytmu
    # return [randint(0, 10 ** 6) for  in range(data_size)]
    a = [randint(0, 100) for i in range(data_size)]
    b = [randint(0, 100) for i in range(data_size)]
    data = a, b
    return data




def solve_problem(data):
 a= data[0]
 b= data[1]
 wynik1 = []
 for i in a:
        wynik = 0
        for ix in b:
            if ix % i == 0:
                wynik += 1
        wynik1.append(wynik)
 return wynik1
pass


def run_tests(generator, solver):
    size = 10
    sizes = []
    times = []
    while size < 10000:
        print(f'testing solver for {size=}')
        data = generator(size)
        REPETITIONS = 400
        time_sum = 0
        for i in range(REPETITIONS):
            st = datetime.now().timestamp()
            ret = solver(data)
            en = datetime.now().timestamp()
            time_sum += (en - st)

        sizes.append(size)
        times.append(time_sum / REPETITIONS * 10 ** 6)
        size *= 2

    return sizes, times


if name == 'main':
    x, y = run_tests(generate_data, solve_problem)

    plt.plot(x, y)
    plt.xlabel("Rozmiar danych")
    plt.ylabel("Czas wykonania (usec)")
    plt.show()