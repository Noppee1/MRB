from random import seed, randint

from src.algo.z3.bb2 import run_tests, visualize


def solve(a: list[int]) -> list[int]:
    i = 0
    i2 = 10
    wynik = []
    while i2 != len(a):
        wynik.append(sum(a[i:i2]))
        i += 10
        i2 += 10
    return max(wynik)

    # unique = set(a)
    # cache = dict()
    #
    # for i_a in unique:
    #     cnt = 0
    #     for i_b in b:
    #         if i_b % i_a == 0:
    #             cnt += 1
    #     cache[i_a] = cnt
    #
    # res = [cache[i_a] for i_a in a]
    return wynik


def generate_data(data_size):
    seed(111)
    mx_num = 10 ** 4
    a = [randint(0, mx_num) for _ in range(data_size)]
    b = [randint(0, mx_num) for _ in range(data_size)]
    return {"a": a, "b": b}


if __name__ == '__main__':
    x, y = run_tests(generate_data, solve, max_size=10**4)
    visualize(x, y)
    # print(solve([2, 5, 7, 9, 2], [4, 8, 18, 27]))