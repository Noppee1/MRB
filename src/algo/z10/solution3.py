import random
import string


def encoder(s: str) -> str:
    word = [i for i in s]
    wyjscie = []
    out = ""

    for i in word:
        wyjscie.append(i + "".join(random.sample(string.ascii_lowercase, 3)) + i)

    for each in range(len(wyjscie)):
        out += wyjscie[each]

    print(out)


encoder('kod')
