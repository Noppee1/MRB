
def decoder(s: str) -> str:
    wyjscie = s[0]
    counter = 1

    idx = 1
    while idx < len(s):
        if s[idx] != wyjscie[-1]:
            counter += 1
        elif s[idx] == wyjscie[-1]:
            if counter + 1 < len(s):
                wyjscie += s[counter + 1]
                counter += 2
                idx += 1
        idx += 1

    if len(s) % 2 != 0 and s[-1] != wyjscie[-1]:
        wyjscie += s[-1]

    print(wyjscie)
    return wyjscie


decoder("ilaidwzpvyufbngdzncgxeozixgnyliecemwlaobjvtmyijbqzehy vpkleuqi geqrfylhvgreusfraxwfegbskdtaćć?ahzyvejs?")