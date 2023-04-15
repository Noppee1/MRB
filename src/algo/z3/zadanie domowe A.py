from random import seed, randint

from src.algo.z3.automat import run_tests, visualize


def largest_sum_10_percent(a: list[int]) -> int:
    segment_length = len(a) // 10
    max_sum = sum(a[:segment_length])
    current_sum = max_sum
    odp = []

    for i in range(1, 10):
        start_index = i * segment_length
        end_index = start_index + segment_length
        if sum(a[start_index:end_index]) > current_sum:
            current_sum = sum(a[start_index:end_index])
            odp.append(a[start_index:end_index])
        max_sum = max(max_sum, current_sum)

    return max_sum, odp[-1]


def generate_data(data_size):
    seed(111)
    mx_num = 10 ** 4
    data_a = [randint(0, mx_num) for _ in range(data_size)]
    # print(data_a)
    return {"a": data_a}


print(largest_sum_10_percent(generate_data(100)['a']))

# if __name__ == '__main__':
#     x, y = run_tests(generate_data, largest_sum_10_percent, max_size=10**4)
#     visualize(x, y)