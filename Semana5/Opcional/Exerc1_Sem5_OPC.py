def fizzbuzz(numero):
    #'FizzBuzz' se o número for divisível por 3 e por 5;
    if numero % 5 == 0 and numero % 3 == 0:
        return 'FizzBuzz'
    #'Fizz' se o número for divisível por 3 e não for divisível por 5;
    elif numero % 3 == 0:
        return 'Fizz'
    #'Buzz' se o número for divisível por 5 e não for divisível por 3;
    elif numero % 5 == 0:
        return 'Buzz'
    #Caso o número não seja divisível 3 e por 5, ela deve devolver o número recebido como parâmetro.
    else:
        return numero
