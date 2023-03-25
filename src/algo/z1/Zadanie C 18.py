from random import seed, randint
from datetime import datetime

from automat import run_tests, visualize




def solve(a: list[int]) -> int:
    max_result = 0
    for i in range(len(a)-1):
        res = a[i] * a[i+1]
        if res > max_result:
            max_result = res

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

print(solve(generate_data(10 ** 4)))

# if __name__ == '__main__':
#     x, y = run_tests(generate_data, solve, max_size=10**4)
#     visualize(x, y)