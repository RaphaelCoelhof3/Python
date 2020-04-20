print ("Digite 3 números em oredem crescente")
numero1 = int(input("Primeiro número: "))
numero2 = int(input("Segundo número: "))
numero3 = int(input("Terceiro número: "))


if numero1 < numero2 < numero3:
    print("Os números estão em ordem crescente")
    print("Bom trabalho")
else:
    print("Os números não estão em ordem crescente")
    print("Por favor, repita a operação")
