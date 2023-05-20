
"""
Słowa sklejamy z sylab w następujący sposób:

słowo:

"abac"

... trzeba złożyć z 2-literowych "sylab"
ab←→ba -> aba
aba←→ac -> abac

(czyli dołączana sylaba 2-literowa ma mieć taką pierwszą literę, jak ostatnia litera słowa do którego jest dołączana)



ababacdad

"""


def split_to_syllables(word: str) -> list[str]:
    output = []
    for letter in range(len(word) - 1):
        output.append(word[letter] + word[letter + 1])
    return output
