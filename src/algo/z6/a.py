
s=['aa', 'a', 'c', 'bb', 'bb', 'bb', 'c']
c=['aa', 'a', 'c', 'bb',]

def are_uni(input):
    if len(set(input)) == len(input):
        print('TURE')
    else:
        print('False')

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


are_uni(s)
are_uni(c)
