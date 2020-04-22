def remove_repetidos (lista):
    L = []
    for i in lista:
        if i not in L:
            L.append(i)
    L.sort()
    return L
