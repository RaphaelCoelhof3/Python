linha = 1
coluna = 1

while linha <= 10:
    while coluna <= 10: #Enquanto "coluna" for menor que 10, multiplique o primeiro valor da linha pelo valor da coluna.
        print(linha * coluna, end= "\t")
        coluna += 1 #Após a primeira multiplicação, some 1 e volte a realizar a terefa de multiplicar este novo valor de coluna pelo vlor da linha.
        # Esgotando-se os valores de coluna, isto é, coluna maior ou igual a 10, 
    linha += 1 #Some mais 1 unidade ao valor de linha. Com esse novo valor volte a fazer a equação anterior.
    print()
    coluna = 1 # é preciso reiniciar o valor da coluna, pois ela terminara na operação anterior com o valor 10. 
