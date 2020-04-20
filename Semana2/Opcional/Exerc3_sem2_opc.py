numero = int(input("Digite um número inteiro: "))

unidade = numero % 10

print("O dígito da unidade é:",unidade)

numero_sem_unid = numero // 10
decimal_do_numero = numero_sem_unid % 10

print("O dígito das dezenas é:",decimal_do_numero)

numero_sem_decimal = numero // 100
centezimal_do_numero = numero_sem_decimal % 10

print("O dígito da centena é:",centezimal_do_numero)
