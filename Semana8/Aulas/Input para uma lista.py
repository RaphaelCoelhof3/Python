#Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros.
#Verifique se tal lista possui elementos repetidos e os remova.

def remove_repetidos (lista):
    L = []
    for i in lista:
        if i not in L:
            L.append(i)
    L.sort()
    return L

#>>>>>>>>

lista = [2, 3, 5, 5, 6, 4, 8, 7, 9, 2, 1]
lista = remove_repetidos(lista)
print(lista)


lista = []
entrada = 1

while entrada != 0:
    entrada = int(input("Digite os valores: "))
    if entrada != 0:
        lista.append(entrada)
    else:
        break

