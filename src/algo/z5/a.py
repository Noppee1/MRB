from src.algo.z4.trains.zadanie_a import extract_destination_info
from random import randint

dane1 = [[1,2], [2,4], [4,3], [3,1], [3, 5]]
dane2 = [(1,2), (2,4), (4,3), (3,1), (3, 5), (5, 1), (4,3)]

def random_travel(at: int, destination: list[list[int]]):
    max_steps = 50
    max_city = max([start for start, end in dane1]) + 1
    i = 0

    while i < max_steps:
        for dest in destination:
            if len(dest) == 1 and at == max_city:
                print('Koniec zabawy')
                exit()
                i += 1

            if len(dest) > 2 and at == dest[0]:
                random_number = randint(1, len(dest) -1)
                at = dest[random_number]
                print(f'skok z {dest[0]} na {dest[random_number]}')
                i += 1

            if dest[0] == at:
                at = dest[1]
                print(f'skok z {dest[0]} na {dest[1]}')
                i += 1




if __name__ == '__main__':
    destination = extract_destination_info(dane2)
    print(destination)
    random_travel(1, destination)
