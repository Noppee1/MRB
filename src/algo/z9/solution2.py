"""
Semanotic versining
https://devopedia.org/images/article/279/7179.1593248779.png

{Major}.{Minor}.{Patch}

np.

'1.3.6' oznacza major=1, minor=3, path=6


"""


def get_latest(versions: list[str]) -> str:
    """
    :return: Latest semantic version from the given `versions`
    """

    return max(versions)


def next_version(version: str, level: int) -> str:
    """
    :param version: Current version
    :param level: Which part should be incremented; 0: major, 1: minor, 2: patch
    :return: Properly incremented version
    """

    a, b, c = version.split(".")

    if level == 0:
        a = str(int(a) + 1)
        b = "0"
        c = "0"

    if level == 1:
        b = str(int(b) + 1)
        c = "0"

    if level == 2:
        c = str(int(c) + 1)

    wyjscie = '.'.join([a, b, c])
    return wyjscie

