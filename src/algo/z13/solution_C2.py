def is_valid_move(x, y):
    return x >= 1 and x <= 8 and y >= 1 and y <= 8


def can_knight_jump(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
        return True

    return False


def min_knight_moves(x1, y1, x2, y2):
    if not (is_valid_move(x1, y1) and is_valid_move(x2, y2)):
        return -1

    if (x1, y1) == (x2, y2):
        return 0

    if can_knight_jump(x1, y1, x2, y2):
        return 1

    ruchy = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    sprawdzone = set()
    kolejka = [(x1, y1, 0)]

    while kolejka:
        x, y, kroki = kolejka.pop(0)

        if (x, y) == (x2, y2):
            return kroki

        for dx, dy in ruchy:
            new_x = x + dx
            new_y = y + dy

            if is_valid_move(new_x, new_y) and (new_x, new_y) not in sprawdzone:
                sprawdzone.add((new_x, new_y))
                kolejka.append((new_x, new_y, kroki + 1))

    return -1


def main():
    try:
        x1, y1 = map(int, input("Podaj współrzędne pola A (oddzielone spacją): ").split())
        x2, y2 = map(int, input("Podaj współrzędne pola B (oddzielone spacją): ").split())

        min_moves = min_knight_moves(x1, y1, x2, y2)

        if min_moves == -1:
            print("Podano nieprawidłowe współrzędne pola.")
        elif min_moves == 0:
            print("Skoczek jest już na docelowym polu.")
        else:
            print(f"Minimalna liczba ruchów skoczka między polami A i B: {min_moves}")

    except ValueError:
        print("Wprowadzono nieprawidłowe dane. Upewnij się, że podano dwie liczby całkowite oddzielone spacją.")


if __name__ == "__main__":
    main()
