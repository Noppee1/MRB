
a = [1,0,-1,-1,0,2,5,0,-2]

def get_min_number_of_operations(a: list[int]) -> int:
    count = 0
    for each in range(0, len(a)):
        if a[each] > 0 and a[each - 1] <= 0:
            count += 1

    return count