numero = int(input("Entre com um número inteiro:"))
ultimo_numero = numero % 10
if (ultimo_numero == 0) or (ultimo_numero == 5):
    print("Buzz")
else:
    print(numero)
