#Avaliação  de desempenho escolar "Para 4 valores de entrada".


Nota1 = float(input("Digite a primeira nota:"))
Nota2 = float(input("Digite a segunda nota:"))
Nota3 = float(input("Digite a terceira nota:"))
Nota4 = float(input("Digite a quarta nota:"))

# Cálculo da MÉDIA:
média = float((Nota1 + Nota2 + Nota3 + Nota4)/4)

# Cálculo da Variânca:
import math
VR = int((Nota1 - média)**2 + (Nota2 - média)**2 + (Nota3 - média)**2 + (Nota4 - média)**2)/4


# Cálculo do Desvio Padrão:
DP = math.sqrt(VR)


print("A média aritmética é", média, ", o Desvio Padrão",DP, "e a Variância:",VR,".")
