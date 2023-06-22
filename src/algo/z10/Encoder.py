import random
import string


def encoder(s: str) -> str:
    word = [i for i in s]
    wyjscie = []
    out = ""

    for i in word:
        exclude = [letter for letter in string.ascii_lowercase if letter != i]
        wyjscie.append(i + "".join(random.sample(exclude, random.randint(0, 10))) + i)

    for each in range(len(wyjscie)):
        out += wyjscie[each]

    print(out)
    return out

encoder('idziemy grać?')
