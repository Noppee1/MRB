from random import seed, randint
from datetime import datetime

from src.algo.z3.automat import run_tests, visualize


def best_multiply(a: list[int]):
    st1 = datetime.now().timestamp()
    sort = sorted(a)
    result = sort[-2] * sort[-1]
    st2 = datetime.now().timestamp()
    time = st2 - st1
    print(f'czas wykonywania 1: {time}')
    return result


def solve(a: list[int]) -> int:
    em1 = datetime.now().timestamp()
    max_result = 0
    for i in range(len(a)-1):
        res = a[i] * a[i+1]
        if res > max_result:
            max_result = res
    em2 = datetime.now().timestamp()
    time1 = em2 - em1
    print(f'czas wykonywania 2: {time1}')
    return max_result


def generate_data(data_size):
    seed(111)
    mx_num = 10 ** 4
    data_a = [randint(0, mx_num) for _ in range(data_size)]
    return data_a

# a=[1,2,3]
# b=[2,2,-3,-3]
# print(best_multiply(a))
# print(best_multiply(b))

print(best_multiply(generate_data(10 ** 4)))
print(solve(generate_data(10 ** 4)))

# if __name__ == '__main__':
#     x, y = run_tests(generate_data, solve, max_size=10**4)
#     visualize(x, y)