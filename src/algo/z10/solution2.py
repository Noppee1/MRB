from random import randint


def zadanie_b(word: str) -> list[int]:
    result = []
    random_number = randint(1, 10)
    result.append(random_number)

    if len(word) != 0:
        for i in word:
            if i == '<':
                result.append(randint(result[-1], 10))
            elif i == '>':
                result.append(randint(1, result[-1]))
    print(result)


zadanie_b('<<>')