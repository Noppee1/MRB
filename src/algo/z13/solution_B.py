def get_area(x1, y1, x2, y2) -> int:

    minx = abs(x1 - x2) + 1
    miny = abs(y1 - y2) + 1

    return minx * miny
