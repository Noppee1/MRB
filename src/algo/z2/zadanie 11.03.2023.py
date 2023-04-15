from datetime import datetime
import matplotlib.pyplot as plt
from random import seed, randint

# Kod zajmuje około 30 sekund na wykonanie !!

def generate_data(data_size):
    a = [randint(1, 100) for _ in range(data_size)]
    b = [randint(1, 100) for _ in range(data_size)]
    data = a, b
    return data

def solve_problem(data):
    a = data[0]
    b = data[1]
    wynik = []
    for ax in a:
        count = 0
        for i in b:
            if i % ax == 0:
                count += 1
        wynik.append(count)
    return wynik

def run_tests(generator, solver):
    size = 10
    sizes = []
    times = []
    while size < 1281:
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


if __name__ == '__main__':
    x, y = run_tests(generate_data, solve_problem)

    plt.plot(x, y)
    plt.xlabel("Rozmiar danych")
    plt.ylabel("Czas wykonania (usec)")
    plt.show()