numero = int((input("Entre com um número inteiro:")))

ultimo_numero = numero % 10

if ((numero % 3 == 0) and ((ultimo_numero == 0) or (ultimo_numero == 5))):
    print("FizzBuzz")
else:
    print(numero)
