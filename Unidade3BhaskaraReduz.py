import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b ** 2) - (4 * a * c)

print("O valor de Delta �:", delta)
raiz1 = (-b + math.sqrt(delta))/(2*a)
raiz2 = (-b - math.sqrt(delta))/(2*a)

if delta == 0:
        print("e por isso h� uma �nica raiz, que �: ", raiz1)
else:
    if delta < 0:
        print("Esta express�o n�o possui raizes reais")
    else:
        print("e por isso h� mais de uma raiz")
        print("A primeira raiz �: ", raiz1)
        print("A segunda raiz �: ", raiz2)
