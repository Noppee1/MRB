s=['aa', 'a', 'c', 'bb']

def are_elements_unique(s):
    if len(set(s)) == len(s):
        return print("seba potwierdza")
    else:
        print('SEBA NIE POTWIERDZA')

are_elements_unique(s)


def find_duplicates(strings):
    d = {}
    duplicates = []
    for s in strings:
        if s not in d:
            d[s] = 1
        else:
            d[s] += 1
            if d[s] == 2:
                duplicates.append(s)
    return duplicates if duplicates else False

duplicates = find_duplicates(s)

if duplicates:
    print("Duplikaty: ", ", ".join(duplicates))
else:
    print("Brak duplikatów")
