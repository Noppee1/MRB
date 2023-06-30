


def get_best_value_package(costs: list[int], values: list[int], max_total_cost: int) -> int:
    N = len(costs)
    wynik = 0

    for k in range(2 ** N):
        koszt = 0
        wartosc = 0

        for i in range(N):
            if k & (1 << i):
                koszt += costs[i]
                wartosc += values[i]

        if koszt <= max_total_cost and wartosc > wynik:
            wynik = wartosc

    return wynik

