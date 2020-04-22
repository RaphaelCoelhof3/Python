import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b ** 2) - (4 * a * c)

print("O valor de Delta é:", delta)

if delta == 0:
    raiz1 = (-b + math.sqrt(delta))/(2*a)
    print("e por isso só há uma única raiz, que é: ", raiz1)
else:
    if delta < 0:
        print("Esta expressão não possui raízes reais")
    else:
        raiz1 = (-b + math.sqrt(delta))/(2*a)
        raiz2 = (-b - math.sqrt(delta))/(2*a)
        print("e por isso há mais de uma raiz")
        print("A primeira raiz é: ", raiz1)
        print("A segunda raiz é: ", raiz2)
