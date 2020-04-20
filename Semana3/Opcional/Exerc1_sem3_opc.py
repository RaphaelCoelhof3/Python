print("Digite os valores de coordenadas x e y dos pontos A e B respectivamente:")

xa = int(input("Coordenda x do ponto A: "))
ya = int(input("Coordenda y do ponto A: "))
xb = int(input("Coordenda x do ponto B: "))
yb = int(input("Coordenda y do ponto B: "))

import math

Hipotenusa = math.sqrt((xb - xa)**2 + (yb - ya)**2)

if Hipotenusa >= 10:
    print("longe")
else:
    print("perto")
