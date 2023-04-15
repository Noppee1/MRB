dane = [(5,'Adam'), (3,'Jane'), (5, 'Xiao'), (2,'Jane')]
dane1= [(1,'Adam'), (2,'Jane'), (3, 'Xiao'), (4,'Jade')]

def unique_id(dane):
    d = {}
    duplicates = []
    for id, name in dane:
        if id not in d:
            d[id] = name
        else:
            duplicates.append([id])
    return print(duplicates) if duplicates else print('brak')


def unique_name(dane):
    d = {}
    duplicates = []
    for id, name in dane:
        if name not in d:
            d[name] = id
        else:
            duplicates.append([name])
    return print(duplicates) if duplicates else print('brak')


unique_id(dane)
unique_id(dane1)

unique_name(dane)
unique_name(dane1)
