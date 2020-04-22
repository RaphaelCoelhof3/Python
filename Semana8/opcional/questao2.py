x = 999999999
lista = []
while x != 0:
    x = int(input("Digite um número: "))
    if x != 0:
        lista.append(x)
    else:
        break
lista.reverse()    
print("")

Quant = len(lista)
print("")
i = 0
while i < Quant:
    print(lista[i])
    i+=1


   

