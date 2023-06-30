def get_min_number_of_operations(a: list[int]) -> int:

    counter = 0
    i = 1

    if a[0] <= 0:
        counter += 1

    while len(a) > i:

        if a[i] < 0:
            if a[i - 1] <= 0:
                i += 1
                continue
            counter += 1
            i += 1
            continue
        i += 1
    return counter